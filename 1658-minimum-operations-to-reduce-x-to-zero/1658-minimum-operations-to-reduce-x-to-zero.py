class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        totalSum = sum(nums)
        target = totalSum - x#target for subarray sum
        if x == 0:
            return 0
        sumCounter = {}
        sumCounter[0] = -1
        tempSum = 0
        maxArrayLen = -1
        for i in range(len(nums)):
            tempSum += nums[i]
            if tempSum not in sumCounter:
                sumCounter[tempSum] = i
            if tempSum - target in sumCounter:
                maxArrayLen = max(maxArrayLen, i-sumCounter[tempSum-target])
        
            
        if maxArrayLen == -1:
            return -1
        return len(nums)-maxArrayLen
            
            
            