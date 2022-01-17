class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p1 = 0
        p2 = 0
        sum = nums[0]
        ans = 0
        for i in range(k-1):
            p2+=1
            sum += nums[p2]
        ans = sum/k
        for i in range(len(nums)-k):
            sum -= nums[p1]
            p1+=1
            sum+=nums[p2+1]
            p2+=1
            ans = max(ans,sum/k)
        return ans
        