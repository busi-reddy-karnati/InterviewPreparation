class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            sub_array_min = nums[i]
            sub_array_max = nums[i]
            for j in range(i, len(nums)):
                sub_array_min = min(sub_array_min, nums[j])
                sub_array_max = max(sub_array_max, nums[j])
                ans += sub_array_max - sub_array_min
        return ans