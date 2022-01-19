def possible(arr, m, k, val):
    num_b = 0
    aux_store = 0
    for i in range(len(arr)):
        if arr[i] <= val:
            # print(i)
            aux_store += 1
        else:
            # print(i)
            aux_store = 0
        if aux_store == k:
            num_b +=1
            aux_store = 0
    # print(val,num_b)
    return num_b >= m
class Solution:               
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # possible(bloomDay,m,k,7)
        # return 1
        if m*k > len(bloomDay):
            return -1
        hi = max(bloomDay)
        lo = 1
        ans = 0
        while lo <= hi:
            mid = (hi+lo)//2
            if possible(bloomDay,m,k,mid):
                # print(bloomDay,m,k,mid)
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans