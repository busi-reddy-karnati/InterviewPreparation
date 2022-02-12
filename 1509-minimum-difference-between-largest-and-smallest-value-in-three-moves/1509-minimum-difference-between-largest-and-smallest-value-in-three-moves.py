class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        self.dp = {}
        if len(nums)<=4:
            return 0
        return self.helper(nums,3,0, len(nums)-1)
    def helper(self, nums, changes, left, right):
        key = (changes,left,right)
        if changes == 0:
            return nums[right]-nums[left]
        if key in self.dp:
            return self.dp[key]
        ans = min(self.helper(nums,changes-1,left+1,right),self.helper(nums,changes-1,left,right-1))
        self.dp[key] = ans
        return ans
        