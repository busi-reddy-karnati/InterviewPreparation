
from multiprocessing.connection import answer_challenge


class Solution:
    def longestPalindrome(self, s: str) -> str:
        odd_index = 0
        ans_len = 0
        ans_string = ""
        n = len(s)
        for i in range(n):
            offset = 0
            while i-offset >=0 and i+offset<n:
                if s[i-offset] != s[i+offset]:
                    break
                if ((2*offset)+1) > ans_len:
                    ans_len = ((2*offset)+1)
                    ans_string = s[i-offset:i+offset+1]
                offset += 1

        for i in range(n-1):
            offset = 0
            while i-offset >= 0 and i+offset+1<n:
                if s[i-offset] != s[i+offset+1]:
                    break
                if ((2*offset)+2) > ans_len:
                    ans_len = ((2*offset)+2)
                    ans_string = s[i-offset:i+offset+2]
                offset += 1
        return ans_string

