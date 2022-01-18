class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or nums[0]>target:
            return 0
        if nums[-1] < target:
            return len(nums)
        hi = len(nums)-1
        lo = 0
        ans = 0
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans