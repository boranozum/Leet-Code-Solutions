from typing import List

class CourseNode:
    def __init__(self, course_id: int, preq_of=None):
        self.preq_of = preq_of
        self.course_id = course_id


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        courses = []

        for course_id in range(numCourses):
            course = CourseNode(course_id=course_id)
            courses.append(course)

        for preq in prerequisites:
            courses[preq[0]].preq_of = preq[1]

        result = []
        for query in queries:
            result.append(self.courseBFS(courses, courses[query[0]], courses[query[1]]))

        return result

    def courseBFS(self, courses: List[CourseNode], source: CourseNode, dest: CourseNode) -> bool:

        queue = []
        queue.append(source)

            while queue:
            course = queue.pop(0)
            if course == dest:
                return True
            if course.preq_of is not None:
                queue.append(courses[course.preq_of])
        return False


s = Solution()
print(s.checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))




