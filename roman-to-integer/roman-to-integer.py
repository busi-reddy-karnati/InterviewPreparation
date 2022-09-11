class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        
        pointer = 0
        
        roman_map = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000
        }
        subs_map = {
            'I':['V','X'],
            'X':['L','C'],
            'C':['D','M']
        }
        while pointer < len(s):
            char = s[pointer]
            if char == 'V' or char == 'L' or char == 'D' or char=="M":
                ans += roman_map[char]
            else:
                if pointer == len(s)-1:#I don't need to see at the subs
                    ans += roman_map[char]
                    return ans
                if s[pointer+1] in subs_map[char]:
                    ans += roman_map[s[pointer+1]]-roman_map[char]
                    pointer += 1
                else:
                    ans += roman_map[char]
            pointer += 1
        return ans