class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        max_possible_length = int(3*(2**(n-1)))
        result = ""

        if k > max_possible_length:
            return ''

        a_root_value = max_possible_length/3/2 + 0.5
        b_root_value = a_root_value+2**(n-1)
        c_root_value = b_root_value+2**(n-1)

        selected_letter = "a"
        root_value = a_root_value
        if max_possible_length/3 < k and k <= 2*max_possible_length/3:
            root_value = b_root_value
            selected_letter = "b"
        elif k > 2*max_possible_length/3:
            root_value = c_root_value
            selected_letter = "c"

        result += selected_letter
        t = int(a_root_value)/2
        while len(result) < n:
            if selected_letter == "a":
                if k < root_value:
                    selected_letter = "b"
                    result += selected_letter
                    root_value -= t

                else:
                    selected_letter = "c"
                    result += selected_letter
                    root_value += t


            elif selected_letter == "b":
                if k < root_value:
                    selected_letter = "a"
                    result += selected_letter
                    root_value -= t
                else:
                    selected_letter = "c"
                    result += selected_letter
                    root_value += t

            elif selected_letter == "c":
                if k < root_value:
                    selected_letter = "a"
                    result += selected_letter
                    root_value -= t
                else:
                    selected_letter = "b"
                    result += selected_letter
                    root_value += t

            t /= 2

        return result


s = Solution()
print(s.getHappyString(10,100))






