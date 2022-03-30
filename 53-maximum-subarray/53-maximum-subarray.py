class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = sumi = nums[0]
        for i in range(1,len(nums)):
            sumi = max(nums[i],nums[i]+sumi)
            maxi = max(sumi,maxi)
        return maxi