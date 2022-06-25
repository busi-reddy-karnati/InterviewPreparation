class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        num_violations = 0
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                if num_violations > 0:
                    print(nums[i-1],nums[i])
                    return False
                num_violations += 1
                if i<2:
                    nums[i-1] = nums[i]
                elif nums[i-2]>nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
        return True