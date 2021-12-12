class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s = s//2
        dp = [False]*(s+1)
        dp[0] = True
        for num in nums:
            for i in range(s,-1,-1):
                if i >= num:
                    dp[i] = dp[i] or dp[i-num]
        return dp[s]