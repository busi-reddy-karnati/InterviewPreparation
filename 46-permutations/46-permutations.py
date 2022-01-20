class Solution:
    ans = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        aux_list = []
        visited = set()
        self.helper(nums,0,aux_list,visited)
        return self.ans
    def helper(self, nums, index, aux_list, visited):
        if index >= len(nums):
            self.ans.append([i for i in aux_list])
        for num in nums:
            if num not in visited:
                visited.add(num)
                aux_list.append(num)
                self.helper(nums,index+1,aux_list, visited)
                visited.remove(num)
                aux_list.pop(-1)
        