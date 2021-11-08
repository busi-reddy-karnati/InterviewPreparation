class Solution:
    def fac(self,n):
        if n == 0:
            return 1
        return n*self.fac(n-1)
    def uniquePaths(self, m: int, n: int) -> int:
        m = m-1
        n = n-1
        return int(self.fac(m+n)/(self.fac(n)*self.fac(m)))