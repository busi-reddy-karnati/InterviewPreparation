class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = {}
        return self.helper(n)
    def helper(self, n):
        if n in self.dp:
            return self.dp[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        ans = self.helper(n-1)+self.helper(n-2)
        self.dp[n] = ans
        return ans