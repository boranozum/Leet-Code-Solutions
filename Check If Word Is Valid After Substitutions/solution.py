class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 3:
            return False

        if s[0] != 'a' or s[-1] != 'c':
            return False

        levels = ['a']
        level = 0

        for i in range(1,len(s)):
            if len(levels) == 0:
                if s[i] != 'a':
                    return False
                level = 0
                levels.append('a')

            elif levels[level] == 'a':
                if s[i] == 'c':
                    return False
                if s[i] == 'a':
                    level+=1
                    levels.append('a')
                else:
                    levels[level] = 'b'

            elif levels[level] == 'b':
                if s[i] == 'b':
                    return False
                if s[i] == 'a':
                    level+=1
                    levels.append('a')
                else:
                    level -= 1
                    levels = levels[:-1]

        if len(levels) == 0:
            return True

        return False




s = Solution()

print(s.isValid("abcabcababcc"))
