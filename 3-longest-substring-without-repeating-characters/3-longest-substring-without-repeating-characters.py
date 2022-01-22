class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        freq = {}
        p1 = 0
        ans = 0
        p2 = 0
        freq[s[0]] = 1
        while p2 < len(s)-1:
            p2+=1
            
            if s[p2] in freq:
                while s[p1] != s[p2]:
                    del freq[s[p1]]
                    p1+=1
                p1+=1
                ans = max(ans,len(freq))
            freq[s[p2]] = 1
            ans = max(ans,len(freq))
        ans = max(ans,len(freq))
        return ans