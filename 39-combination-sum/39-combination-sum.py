class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        path = []
        nums.sort()
        self.helper(nums,target,0,path)
        return self.ans
    def helper(self,nums,target,ind,path):
        if target == 0:
            self.ans.append([num for num in path])
        if ind >= len(nums) or target < nums[ind]:
            return
        itr = 0
        num = nums[ind]
        while itr*num <= target:
            self.helper(nums,target-(itr*num),ind+1,path)
            itr+=1
            path.append(num)
        for i in range(itr):
            path.pop(-1)
        
        