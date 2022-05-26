class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        temp_sum = nums[0]
        for i in range(1,n):
            temp_sum = max(temp_sum+nums[i], nums[i])
            ans = max(ans,temp_sum)
        return ans