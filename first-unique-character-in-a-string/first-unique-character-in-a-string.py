class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for char in s:
            hash_map[char] = hash_map.get(char,0)+1
        for i, char in enumerate(s):
            if hash_map[char] == 1:
                return i
        return -1