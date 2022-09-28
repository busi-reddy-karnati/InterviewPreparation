class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        if len(nums)==1:
            return 0
        if len(nums) == 2:
            if nums[1]>nums[0]:
                return 1
            return 0
        while start <= end:
            if start == end-1:
                if nums[end]>nums[start]:
                    return end
                return start
            mid = (start+end)//2
            if mid == 0 or mid == len(nums)-1:
                return mid
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid+1]>nums[mid]:
                start = mid+1
            else:
                end = mid-1
        return -1