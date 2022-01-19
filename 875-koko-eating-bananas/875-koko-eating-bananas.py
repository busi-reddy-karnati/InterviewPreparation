from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = sum(piles)
        lo = 1
        ans = 0
        while hi>=lo:
            mid = (hi+lo)//2
            if possible(mid,piles,h):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans
def possible(val, piles, h):
    num_hours = 0
    for num in piles:
       num_hours += ceil(num/val)
    return num_hours <=h
        