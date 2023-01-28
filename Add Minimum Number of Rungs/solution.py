from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:

        rungs = [0] + rungs

        result = 0

        for i in range(1,len(rungs)):
            distance_between_rungs = rungs[i]-rungs[i-1]

            if distance_between_rungs > dist:

                if distance_between_rungs % dist == 0:
                    result += int(distance_between_rungs/dist)-1

                else:
                    rungs_to_be_added = int(distance_between_rungs/dist)
                    result += rungs_to_be_added

        return result

s = Solution()
print(s.addRungs([1,3,5,10], 2))
