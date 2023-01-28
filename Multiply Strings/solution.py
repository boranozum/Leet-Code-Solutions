class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return self.integerToString(self.stringToInteger(num1)*self.stringToInteger(num2))

    def stringToInteger(self, num: str) -> int:
        base = 1
        result = 0
        for i in range(len(num)-1, -1, -1):
            result += base*(ord(num[i])-48)
            base *= 10

        return result

    def integerToString(self, num: int) -> str:

        if num == 0:
            return "0"

        base = 1
        result = ""

        while base <= num:
            digit = int((num%(base*10))/base)
            base *= 10
            result = chr(48+digit) + result

        return result

s = Solution()
print(s.multiply("0","0"))



