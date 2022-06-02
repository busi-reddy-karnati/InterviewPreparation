class Solution:
    ans = []
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.solve(candidates, target, [],0)
        return self.ans
    def solve(self, nums, target, temp,index):
        
        if index >= len(nums):
            if sum(temp) == target:
                self.ans.append([i for i in temp])
            return 
        
        insert_count = 0
        self.solve(nums,target,temp,index+1)
        while True:
            if sum(temp)+nums[index] > target:
                break
            temp.append(nums[index])
            insert_count += 1
            self.solve(nums,target,temp,index+1)
        for i in range(insert_count):
            temp.pop()
        
            
        