class Solution:
    f = {1:1,2:2}
    g = {1:1}
    def ffun(self,n):
        if n in self.f:
            return self.f[n]
        ans = self.ffun(n-1)+self.ffun(n-2)+2*self.gfun(n-2)
        self.f[n] = ans
        return ans
    def gfun(self,n):
        if n in self.g:
            return self.g[n]
        ans = self.gfun(n-1)+self.ffun(n-1)
        self.g[n] = ans
        return ans
    def numTilings(self, n: int) -> int:
        return self.ffun(n)%1000000007