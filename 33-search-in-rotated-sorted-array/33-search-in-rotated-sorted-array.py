class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            
            if nums[end] < nums[mid]:
                if nums[mid] < target:
                    start = mid+1
                else:
                    if nums[end]>=target:
                        start = mid+1
                    else:
                        end = mid-1
            else:
                if nums[mid] > target:
                    end = mid-1
                else:
                    if nums[end] >= target:
                        start = mid + 1
                    else:
                        end = mid - 1
        return -1