class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def helper(x,y):
            if x == n-1 or y == m-1:
                return 1
            if (x,y) in dp:
                return dp[(x,y)]
            ans = helper(x+1,y)+helper(x,y+1)
            dp[(x,y)] = ans
            return ans
        return helper(0,0)
            