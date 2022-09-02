class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sum = nums[0]
        sub_array_sum = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            if sub_array_sum + num > num:
                sub_array_sum = sub_array_sum + num
            else:
                sub_array_sum = num
            max_sum = max(max_sum, sub_array_sum)
        return max_sum