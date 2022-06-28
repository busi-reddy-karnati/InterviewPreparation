class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t)) >1:return False
        if s == t:
            return False
        p1 = 0
        p2 = 0
        while p1<len(s) and p2<len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                return self.sameString(s[p1:],t[p2+1:]) or self.sameString(s[p1+1:],t[p2:]) or self.sameString(s[p1+1:],t[p2+1:])
        return True
    def sameString(self, s, t):
        return s==t