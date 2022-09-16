from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums)-1
        pivot_index = -1
        while pivot_index != len(nums)-k:
            ptr = left #ptr stores the less than or equal
            pivot = nums[right]
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            pivot_index = ptr
            print(pivot_index, right)
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            if pivot_index > len(nums)-k:
                right = pivot_index-1
            if pivot_index < len(nums)-k:
                left = pivot_index+1
        return nums[pivot_index]