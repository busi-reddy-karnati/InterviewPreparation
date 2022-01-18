class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [left(nums,target),right(nums,target)]
def left(nums,target):
    ans = -1
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target:
            ans = mid
            hi = mid-1
        elif nums[mid] > target:
            hi = mid-1
        else:
            lo = mid+1
    return ans
def right(nums,target):
    ans = -1
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target:
            ans = mid
            lo = mid+1
        elif nums[mid] > target:
            hi = mid-1
        else:
            lo = mid+1
    return ans