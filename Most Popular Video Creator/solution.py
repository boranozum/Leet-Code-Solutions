from typing import List

class Solution:
    def lexicographicalCompare(self, a: str, b: str) -> bool:
        if len(a) < len(b):
            return True
        elif len(a) > len(b):
            return False
        else:
            for i in range(len(a)):
                if a[i] < b[i]:
                    return True
                elif a[i] > b[i]:
                    return False
            return False

    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:

        popularity = {}
        result = []

        n = len(views)
        max_viewed = ""
        max_view_count = -1
        max_popular = -1

        for i in range(n):
            creator = creators[i]
            video_id = ids[i]
            view = views[i]

            if creator in popularity.keys():

                popularity[creator]["views"] += view

                if view > popularity[creator]["most_viewed"]["views"]:
                    popularity[creator]["most_viewed"]["id"] = video_id
                    popularity[creator]["most_viewed"]["views"] = view
                elif view == popularity[creator]["most_viewed"]["views"]:
                    if self.lexicographicalCompare(video_id, popularity[creator]["most_viewed"]["id"]):
                        popularity[creator]["most_viewed"]["id"] = video_id


            else:
                d = {"views": view, "most_viewed": {"id": video_id,"views": view}}
                popularity[creator] = d

            if popularity[creator]["views"] > max_popular:
                max_popular = popularity[creator]["views"]

        for creator in popularity.keys():
            if popularity[creator]["views"] == max_popular:
                result.append([creator, popularity[creator]["most_viewed"]["id"]])

        return result

s = Solution()

print(s.mostPopularCreator(["bb","bb"], ["baa","bba"], [1,0]))







