class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dp={}
        return self.helper(nums,0)
    def helper(self,nums,index):
        if index in self.dp:
            return self.dp[index]
        if index>=len(nums):
            return 0
        ans = max(nums[index]+self.helper(nums,index+2),self.helper(nums,index+1))
        self.dp[index] = ans
        return ans