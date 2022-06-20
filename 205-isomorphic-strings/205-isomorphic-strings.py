class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = {}
        rhmap = {}
        for i in range(len(s)):
            if s[i] in hmap and hmap[s[i]]!=t[i]:
                return False
            if t[i] in rhmap and rhmap[t[i]] != s[i]:
                return False
            hmap[s[i]] = t[i]
            rhmap[t[i]] = s[i]
        return True