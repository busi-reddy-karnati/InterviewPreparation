class Solution:
    dp = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.dp = {}
        return self.helper(nums,target,0,0)
    def helper(self,nums,target,index,computed_sum):
        if (index,computed_sum) in self.dp:
            return self.dp[(index,computed_sum)]
        if index == len(nums) and computed_sum == target:
            return 1
        if index == len(nums):
            return 0
        positives = self.helper(nums,target,index+1,computed_sum+nums[index])
        negatives = self.helper(nums,target,index+1,computed_sum-nums[index])
        ans = positives+negatives
        self.dp[(index,computed_sum)] = ans
        return ans
        