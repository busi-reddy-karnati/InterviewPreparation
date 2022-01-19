class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        ans = -1
        hi = sum(nums)
        lo = max(nums)
        while hi >= lo:
            mid = (hi+lo)//2
            if possible(mid,nums,m):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans
def possible(val, arr, segs):
    segs_here = 0
    aux_sum = 0
    for i in range(len(arr)):
        aux_sum += arr[i]
        if aux_sum > val:
            aux_sum = arr[i]
            segs_here += 1
    segs_here += 1
    return segs_here <= segs