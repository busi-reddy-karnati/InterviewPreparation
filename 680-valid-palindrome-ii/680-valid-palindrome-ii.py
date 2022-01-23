class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.helper(s,0,len(s)-1,0)
    def helper(self,s,start,end,mods):
        if start >= end:
            return True
        
        if s[start] == s[end]:
            return self.helper(s,start+1,end-1,mods)
        else:
            if mods > 0:
                return False
            return self.helper(s,start+1,end,mods+1) or self.helper(s,start,end-1,mods+1)