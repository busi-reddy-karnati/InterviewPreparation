class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #1. Find all subarrays and see which has the highest sum. O(n2), O(n)
        #2. Using sliding window, Find maximum subarray in all sliding windows O(n2), O(1)
        #3. Use Kadanes Algorithm. Either we take an element to be appended to the previous subarray or start fresh from here O(n), O(1)
        if not nums:
            return 0
        temp_sum = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            temp_sum = max(temp_sum+nums[i], nums[i])
            ans = max(temp_sum, ans)
        return ans