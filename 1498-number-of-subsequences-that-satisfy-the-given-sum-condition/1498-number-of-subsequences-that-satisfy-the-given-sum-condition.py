class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        p1 = 0
        p2 = len(nums)-1
        ans = 0
        mod = (10**9)+7
        while p1<=p2:
            cal_sum = nums[p1]+nums[p2]
            if cal_sum <= target:
                ans = (ans+(2**(p2-p1))%mod)%mod
                p1+=1
            else:
                p2-=1
        return ans
        