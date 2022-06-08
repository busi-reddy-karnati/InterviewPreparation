class Solution:
    def isPalindrome(self,s):
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        return True
    def removePalindromeSub(self, s: str) -> int:
        if self.isPalindrome(s):
            return 1
        return 2
        