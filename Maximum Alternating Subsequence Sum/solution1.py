from typing import List


class Solution:

    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = [[-1 for i in range(len(nums))],[-1 for i in range(len(nums))]]
        return self.helper(dp, 0, nums, True)


    def helper(self, dp: List[List[int]], i: int, nums: List[int], positive: bool) -> int:
        if i >= len(nums):
            return 0
        if dp[positive][i] != -1:
            return dp[positive][i]

        current_number = nums[i]
        if not positive:
            current_number *= -1

        return max(current_number + self.helper(dp, i+1, nums, not positive), self.helper(dp, i+1, nums, positive))



s = Solution()
print(s.maxAlternatingSum([5,6,7,8]))