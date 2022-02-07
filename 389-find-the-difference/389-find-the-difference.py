class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_map_t = {}
        for char in t:
            if char not in char_map_t:
                char_map_t[char] = 1
            else:
                char_map_t[char] += 1
        for char in s:
            char_map_t[char] -= 1
        for key in char_map_t:
            if char_map_t[key] > 0:
                return key
        
            