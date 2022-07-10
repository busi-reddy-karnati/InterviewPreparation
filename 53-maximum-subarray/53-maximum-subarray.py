class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #1. Find all subarrays and see which has the highest sum. O(n2), O(n)
        #2. Using sliding window, Find maximum subarray in all sliding windows O(n2), O(1)
        #3. Use Kadanes Algorithm. Either we take an element to be appended to the previous subarray or start fresh from here O(n), O(1)
        #4 Dp O(n), O(n)
        dp = []
        dp.append(nums[0])
        ans = nums[0]
        for i in range(1,len(nums)):
            temp = nums[i]
            if dp[-1] > 0:
                temp += dp[-1]
            dp.append(temp)
            ans = max(ans,temp)
        return ans