class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = 0
        end = 0
        charset = set()
        while end < len(s):
            if s[end] not in charset:
                charset.add(s[end])
                end += 1
                ans = max(ans,end-start)
            else:
                while s[start] != s[end]:
                    charset.remove(s[start])
                    start += 1
                charset.remove(s[start])
                start += 1
        return ans
        