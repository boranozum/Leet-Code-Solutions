from typing import List

class CourseNode:
    def __init__(self, course_id: int):
        self.preq_of = []
        self.course_id = course_id


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses = []

        for course_id in range(numCourses):
            course = CourseNode(course_id=course_id)
            courses.append(course)

        for preq in prerequisites:
            courses[preq[0]].preq_of.append(preq[1])

        result = []
        for query in queries:
            result.append(self.courseBFS(courses, courses[query[0]], courses[query[1]]))

        return result

    def courseBFS(self, courses: List[CourseNode], source: CourseNode, dest: CourseNode) -> bool:

        visited = set()
        queue = [source]

        while queue:
            current = queue.pop(0)
            if current.course_id == dest.course_id:
                return True

            for preq in current.preq_of:
                if preq not in visited:
                    queue.append(courses[preq])
                    visited.add(preq)

        return False



