class Solution:
    subsets_set = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets_set = []
        self.all_permutations(nums,0,[])
        return (self.subsets_set)
    
    def all_permutations(self,nums,index, temp_list):
        
        if index >= len(nums):
            self.subsets_set.append([i for i in temp_list])
            return
        self.all_permutations(nums,index+1,temp_list)
        temp_list.append(nums[index])
        self.all_permutations(nums,index+1,temp_list)
        temp_list.pop()
        