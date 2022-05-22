class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = [i for i in range(len(nums))]
        nums = list(sorted(zip(indices,nums), key=lambda x:x[1]))
        p1 = 0
        p2 = len(nums)-1
        while True:
            sum = nums[p1][1]+nums[p2][1]
            # print(sum)
            if  sum == target:
                return [nums[p1][0],nums[p2][0]]
            if sum>target:
                p2-=1
            else:
                p1+=1
        
        
                
        