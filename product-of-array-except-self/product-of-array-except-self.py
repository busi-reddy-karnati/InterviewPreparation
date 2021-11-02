class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zc = nums.count(0)
        if zc>1:
            return [0]*len(nums)
        
        for num in nums:
            if num != 0:
                prod *= num
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = prod
            else:
                if zc==1:
                    nums[i] = 0
                else:
                    nums[i] = int(prod/nums[i])
        return nums
            