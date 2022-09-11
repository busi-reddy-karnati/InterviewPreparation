class Solution:
    def myAtoi(self, s: str) -> int:
        pointer = 0
        ans = 0
        sign = 1 # This is the number we multiply
        seen_num = False
        while pointer < len(s) and s[pointer] == " ":
            pointer += 1
        if pointer < len(s) and s[pointer] == '-':
            sign = -1
            pointer += 1
        elif pointer < len(s) and s[pointer] == '+':
            sign = 1
            pointer += 1
        while pointer < len(s) and s[pointer].isnumeric():
            ans = ans*10 + int(s[pointer])
            pointer += 1
        ans = sign*ans
        if ans < -((2)**31):
            print("en")
            ans = -((2)**31)
        if ans > (2**31)-1:
            ans = (2**31)-1
        return ans