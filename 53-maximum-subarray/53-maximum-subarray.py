class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp_sum = nums[0]
        ans = temp_sum
        for i in range(1,len(nums)):
            temp_sum = max(temp_sum+nums[i],nums[i])
            ans = max(ans,temp_sum)
        return ans
        