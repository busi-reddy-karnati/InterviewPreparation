class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = list(num)
        if k >= len(nums):
            return "0"
        for i in range(k):
            self.helper(nums)
        return str(int("".join(nums)))
    def helper(self,nums):        
        for i in range(len(nums)-1):
            if int(nums[i]) > int(nums[i+1]):
                nums.pop(i)
                return
        nums.pop(-1)