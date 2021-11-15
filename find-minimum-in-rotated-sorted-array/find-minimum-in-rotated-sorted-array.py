class Solution:
    def findMin(self, a: List[int]) -> int:
        hi = len(a)-1
        lo = 0
        while lo<hi:
            mid = int((hi+lo)/2)
            if a[mid]<a[mid-1]:
                return a[mid]
            if a[hi] > a[mid]:
                hi = mid-1
            else:
                lo=mid+1
        return a[lo]