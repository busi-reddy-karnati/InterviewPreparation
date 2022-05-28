class Solution:
    global_dp = {}
    def climbStairs(self, n: int) -> int:
        if n in self.global_dp:
            return self.global_dp[n]   
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.global_dp[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.global_dp[n]
    