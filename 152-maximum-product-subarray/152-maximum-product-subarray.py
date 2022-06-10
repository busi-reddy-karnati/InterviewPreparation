class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        max_negative = ans
        max_positive = ans
        for i in range(1,len(nums)):
            temp_negative = min(max_positive*nums[i],max_negative*nums[i], nums[i])
            max_positive = max(max_positive*nums[i],max_negative*nums[i], nums[i])
            max_negative = temp_negative
            ans = max(ans,max_positive,max_negative)
        return ans