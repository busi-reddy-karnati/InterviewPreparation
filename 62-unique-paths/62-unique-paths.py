from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp solution
#         if m < 1 or n < 1:
#             return 0
#         if m == 1 or n == 1:
#             return 1
        
#         #Going to m,n can be from (m-1,n) or (m,n-1)
#         return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        downs = m-1
        rights = n-1
        ans = 1
        init = downs+rights
        mini = min(downs,rights)
        for i in range(mini):
            ans = ans*(init-i)
        
        return int(ans/factorial(mini))