import math
class Solution:
    def lastStoneWeightII(self, nums: List[int]) -> int:
        s = sum(nums)
        h_s = math.ceil(s/2)
        n = len(nums)
        dp = [[False for i in range(h_s+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for j in range(1,h_s+1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        index = n
        for i in range(h_s):
            if dp[index][h_s-i]:
                sum_one = h_s-i
                sum_two = s-sum_one
                return abs(sum_one-sum_two)
        return nums[0]