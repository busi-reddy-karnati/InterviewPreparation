def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans
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
        return int((factorial(downs+rights)/((factorial(downs))*(factorial(rights)))))