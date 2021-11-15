class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)-2):
            num = nums[i]
            p1 = i+1
            p2 = len(nums)-1
            while p1<p2:
                if nums[p1]+nums[p2] == (-1*num):
                    ans.add(tuple(sorted((nums[p1],nums[p2],num))))
                if nums[p1]+nums[p2] > -1*num:
                    p2-=1
                else:
                    p1+=1
        ans_list = []
        for l in ans:
            ans_list.append(list(l))
        return ans_list
                
                
        