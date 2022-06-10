class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        ans = 0
        charset = set()
        while p2 < len(s):
            if s[p2] in charset:
                while s[p1] != s[p2]:
                    charset.remove(s[p1])
                    p1+=1
                p1+=1
            charset.add(s[p2])
            p2+=1
            ans = max(ans,len(charset))
        return ans