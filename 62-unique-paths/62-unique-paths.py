class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fac(k):
            ans = 1
            for i in range(1,k+1):
                ans = ans*i
            return ans
        def find_ans():
            s = m+n
            mini = min(m,n)
            maxi = max(m,n)
            ret = 1
            for i in range(s,maxi,-1):
                ret = ret*i
            return int(ret/fac(mini))
        m = m-1
        n = n-1
        return find_ans()
            