class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if mid == 0:
                print(nums[mid+1],nums[mid])
                if nums[mid+1] > nums[mid]:
                    return mid+1
                return mid
            if mid == len(nums)-1:
                return mid
            if (nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]):
                return mid
            if nums[mid+1] > nums[mid]:
                lo = mid+1
            elif nums[mid-1] > nums[mid]:
                hi = mid-1
            