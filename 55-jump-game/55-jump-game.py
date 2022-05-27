class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxi = 0
        for i in range(n):
            if maxi < i:
                return False
            if nums[i]+i >= n-1:
                return True
            maxi = max(maxi,i+nums[i])
            
            
            