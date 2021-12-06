class Solution:
    def give(self,nums):
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                return i
        return -1
    def find(self,nums,num):
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > num:
                return i
            
    def nextPermutation(self, nums: List[int]) -> None:
        index = self.give(nums)
        if index == -1:#handled
            for i in range(int(len(nums)/2)):
                nums[i],nums[len(nums)-1-i] = nums[len(nums)-1-i],nums[i]
            return
        swap_position = self.find(nums,nums[index])
        # print(index,swap_position)
        nums[index],nums[swap_position] = nums[swap_position],nums[index]
        # print(nums)
        end = len(nums)-1
        start = index+1
        while start <= end:
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1
        return nums