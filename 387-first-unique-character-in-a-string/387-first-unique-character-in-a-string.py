from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        smap = defaultdict(int)
        for char in s:
            smap[char] += 1
        for i in range(len(s)):
            if smap[s[i]] == 1:
                return i
        return -1