from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        odd_finish = 0
        even_finish = 0

        for num in nums:
            odd_finish, even_finish = [max(odd_finish, even_finish-num), max(even_finish, odd_finish+num)]

        return even_finish


s = Solution()
print(s.maxAlternatingSum([4,2,5,3]))