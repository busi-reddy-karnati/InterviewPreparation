class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_len = 0
        ans = ""
        n = len(s)
        for i in range(n):
            x = 0
            while i-x >=0 and i+x<n:
                if s[i+x] != s[i-x]:
                    break
                x+=1
            temp = s[i-x+1:i+x]
            if len(temp) > best_len:
                best_len = len(temp)
                ans = temp
        for i in range(n-1):
            x = 0
            while i-x >=0 and i+x+1<n:
                if s[i-x] != s[i+x+1]:
                    break
                x+=1
            temp = s[i-x+1:i+x+1]
            if len(temp) > best_len:
                best_len = len(temp)
                ans = temp
        return ans