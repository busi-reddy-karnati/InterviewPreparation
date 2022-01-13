import math
def ncr(n,r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(ncr(m+n-2,n-1))
    