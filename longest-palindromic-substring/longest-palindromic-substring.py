class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ans = 0
        for i in range(len(s)):
            x = i
            ptr = 0
            while x + ptr < len(s) and x - ptr >= 0 and s[x+ptr]==s[x-ptr]:
                if (2*ptr)+1 > max_len:
                    ans = s[x-ptr:x+ptr+1]
                    max_len = (2*ptr)+1
                ptr += 1
        for i in range(len(s)-1):
            x = i
            y = i+1
            ptr = 0
            while x-ptr >= 0 and y + ptr<len(s) and s[x-ptr] == s[y+ptr]:
                # print(x,y,ptr)
                if (y+ptr-x+ptr+1) > max_len:
                    max_len = y+ptr-x+ptr+1
                    ans = s[x-ptr:y+ptr+1]
                ptr += 1
        return ans