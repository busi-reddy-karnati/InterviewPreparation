class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def helper(ind, temp):
            nonlocal subsets
            if ind == len(nums):
                subsets.append([num for num in temp])
                return
            helper(ind+1, temp)
            temp.append(nums[ind])
            helper(ind+1, temp)
            temp.pop()
        
        helper(0, [])
        return subsets
        