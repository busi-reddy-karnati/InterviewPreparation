class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp = {}
        return self.helper(nums,0)
    def helper(self, nums, index):
        if index >= len(nums):
            return 0
        if index in self.dp:
            return self.dp[index]
        ans = max(self.helper(nums,index+1), self.helper(nums,index+2)+nums[index])
        self.dp[index] = ans
        return ans