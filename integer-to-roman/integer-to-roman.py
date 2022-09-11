class Solution:
    def intToRoman(self, num: int) -> str:
        roman_map = {
            1000: "M",
            2000: "MM",
            3000: "MMM",
            900: "CM",
            800: "DCCC",
            700: "DCC",
            600: "DC",
            500: "D",
            400: "CD",
            300: "CCC",
            200: "CC",
            100: "C",
            90: "XC",
            80: "LXXX",
            70: "LXX",
            60: "LX",
            50: "L",
            40: "XL",
            30: "XXX",
            20: "XX",
            10: "X",
            9: "IX",
            8: "VIII",
            7: "VII",
            6: "VI",
            5: "V",
            4: "IV",
            3: "III",
            2: "II",
            1: "I",
            0: ""
        }
        num_list = []
        mul = 1
        while num > 0:
            num_list.append((num%10)*mul)
            mul*=10
            num = num //10
        num_list.reverse()
        ans = ""
        for num in num_list:
            ans = ans + roman_map[num]
        return ans