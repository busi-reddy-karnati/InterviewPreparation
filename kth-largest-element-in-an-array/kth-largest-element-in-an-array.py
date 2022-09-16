from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums)-1
        pivot_index = -1 # making this 0 will give an error if we want len(nums) biggest number as the logic won't make it to the while loop 
        while pivot_index != len(nums)-k:
            ptr = left #ptr stores the less than or equal
            pivot = nums[right]
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            pivot_index = ptr
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            if pivot_index > len(nums)-k:
                right = pivot_index-1
            if pivot_index < len(nums)-k:
                left = pivot_index+1
        return nums[pivot_index]