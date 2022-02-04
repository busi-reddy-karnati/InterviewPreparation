class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total_sum = {}
        total_sum[0] = -1
        sum = 0
        ans = 0
        for i,num in enumerate(nums):
            if num == 0:
                sum -= 1
            else:
                sum +=1
            if sum in total_sum:
                ans = max(ans,i-total_sum[sum])
            else:
                total_sum[sum] = i
        return ans
                
        