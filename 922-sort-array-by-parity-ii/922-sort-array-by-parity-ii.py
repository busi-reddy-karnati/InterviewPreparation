class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_p = 1
        even_p = 0
        p = 0
        while p < len(nums):
            if p%2 and nums[p]%2:
                p+=1
                continue
            elif not p%2 and not nums[p]%2:
                p+=1
                continue
            if nums[p]%2 == 1:
                nums[p],nums[odd_p] = nums[odd_p],nums[p]
                odd_p+=2
            else:
                nums[p],nums[even_p] = nums[even_p],nums[p]
                even_p+=2
        return nums
        