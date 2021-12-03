class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            temp = max(maxi*nums[i],mini*nums[i],nums[i])
            mini = min(maxi*nums[i],mini*nums[i],nums[i])
            maxi = temp
            ans = max(ans,mini,maxi)
        return ans