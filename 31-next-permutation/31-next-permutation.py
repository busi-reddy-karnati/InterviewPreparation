class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i-1] < nums[i]:
                
                idx = i-1
                for j in range(n-1,i-1,-1):
                    if nums[j] > nums[idx]:
                        nums[idx],nums[j] = nums[j],nums[idx]
                        nums[idx+1:] = nums[idx+1:][::-1]
                        return
        nums[:] = nums[:][::-1]      