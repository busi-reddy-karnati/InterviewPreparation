class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        subset = []
        self.helper(nums,0,subset)
        return self.ans
    def helper(self,nums,index,subset):
        if index == len(nums):
            self.ans.append([num for num in subset])
            return
        subset.append(nums[index])
        self.helper(nums,index+1,subset)
        subset.pop(-1)
        self.helper(nums,index+1,subset)
        