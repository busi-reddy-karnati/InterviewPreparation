class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        temp = []
        def helper(ind):
            nonlocal subsets
            if ind == len(nums):
                subsets.append(temp.copy())
                return
            helper(ind+1)
            temp.append(nums[ind])
            helper(ind+1)
            temp.pop()
        
        helper(0)
        return subsets
        