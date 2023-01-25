class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ""
        current_numeric_value = 0
        for i in range(n-1):
            for j in range(98, 124):

                remaining = k - current_numeric_value - j + 97
                max_put = (n-1-i)*26

                if remaining <= max_put:
                    result += chr(j-1)
                    current_numeric_value += j-97
                    break

        result += chr(96+k-current_numeric_value)
        return result

s = Solution()
print(s.getSmallestString(5,73))

