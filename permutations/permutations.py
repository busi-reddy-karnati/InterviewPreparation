
class Solution:
    def helper(self,nums,start):
        if start == len(nums):
            return [[]]
        ret = []
        for i in range(start,len(nums)):
            nums[start],nums[i] = nums[i],nums[start]
            perms = self.helper(nums,start+1)
            for perm in perms:
                perm.append(nums[start])
            ret.extend(perms)
            nums[start],nums[i] = nums[i],nums[start]
        return ret
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums,0)
        