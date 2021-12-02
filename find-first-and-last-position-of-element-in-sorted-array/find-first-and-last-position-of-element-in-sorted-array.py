
class Solution:
    def first(self,a,target):
        hi = len(a)-1
        lo = 0
        ans = -1
        while lo <=hi:
            mid = int((lo+hi)/2)
            if a[mid] == target:
                ans = mid
                hi = mid-1
            elif a[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        
        return ans
    def last(self,nums,target):
        ans = -1
        hi = len(nums)-1
        lo = 0
        while hi>=lo:
            mid = int((lo+hi)/2)
            if nums[mid] == target:
                ans = mid
                lo = mid+1
            elif nums[mid]>target:
                hi = mid-1
            else:
                lo = mid+1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first(nums,target),self.last(nums,target)]