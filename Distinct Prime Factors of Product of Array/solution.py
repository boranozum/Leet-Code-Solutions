from typing import List


class Solution:

    def nextPrime(self, num: int) -> int:

        next_num = num+1
        square = round(next_num**.5)

        while True:
            for i in range(2, square+1):
                if next_num % i == 0:
                    next_num+=1
                    break
            else:
                return next_num

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        max_element = max(nums)
        memo = {}
        result = []

        for i in range(max_element+1):
            memo[i] = []

        for num in nums:
            prime_number = 2
            temp = num
            if len(memo[num]) != 0:
                continue
            while temp != 1:
                if temp % prime_number == 0:
                    temp /= prime_number
                    memo[num].append(prime_number)
                    if len(memo[temp]) != 0:
                        memo[num] += memo[temp]
                        break
                else:
                    prime_number = self.nextPrime(prime_number)

            result += memo[num]

        return len(set(result))



s = Solution()
print(s.distinctPrimeFactors([1000,1000,1000,1000]))