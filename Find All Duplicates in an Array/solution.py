from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        num_array = [-1 for i in range(len(nums)+1)]
        result = []

        for i in range(len(nums)):
            if num_array[nums[i]] == -1:
                num_array[nums[i]] = i

            else:
                result.append(nums[i])

        return result


s = Solution()
print(s.findDuplicates([5,4,6,7,9,3,10,9,5,6]))
