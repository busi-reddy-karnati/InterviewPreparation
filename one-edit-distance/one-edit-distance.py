class Solution:
    def check_insert(self,s,t):
        # print(s,t)
        chgs = 0
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2<len(t):
            if s[p1] != t[p2]:
                if chgs > 0:
                    return False
                p1+=1
                chgs += 1
            else:
                p1+=1
                p2+=1
        # print(chgs)
        return (chgs==1)or(p1==p2)
    def check_update(self,s,t):
        chgs = 0
        for i in range(len(s)):
            if s[i]!=t[i]:
                if chgs > 0:
                    return False
                chgs+=1
        return chgs==1
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s)-len(t))>1:
            return False
        if len(s) > len(t):
            return self.check_insert(s,t)
        elif len(t)>len(s):
            return self.check_insert(t,s)
        return self.check_update(s,t)