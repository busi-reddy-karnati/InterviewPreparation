class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        index_map = {}
        for i in range(len(nums)):
            index_map[nums[i]] = i
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                num3 = -(nums[i]+nums[j])
                if num3 in index_map and index_map[num3] not in {i,j}:
                    l = tuple(sorted((num1, num2, num3)))
                    ans.add(l)
        return [list(i) for i in ans]