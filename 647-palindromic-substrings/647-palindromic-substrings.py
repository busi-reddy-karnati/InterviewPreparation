class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        ans = 0
        for i in range(n):
            p1 = i
            p2 = i
            while p1>=0 and p2<n:
                if s[p1]!=s[p2]:
                    break
                ans += 1
                p1-=1
                p2+=1
        for i in range(n-1):
            p1 = i
            p2 = i+1
            while p1>=0 and p2<n:
                if s[p1]!=s[p2]:
                    break
                p1-=1
                p2+=1
                ans += 1
        return ans
        