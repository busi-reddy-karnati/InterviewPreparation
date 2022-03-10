class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        p1 = 0
        p2 = 1
        chars = set()
        ans = 1
        chars.add(s[p1])
        while p2 < len(s):
            if s[p2] in chars:
                while s[p1] != s[p2]:
                    chars.remove(s[p1])
                    p1+=1
                p1+=1
            chars.add(s[p2])
            ans = max(ans,len(chars))
            p2+=1
        return ans
        