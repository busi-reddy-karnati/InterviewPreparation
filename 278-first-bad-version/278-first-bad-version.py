# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if isBadVersion(mid):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans