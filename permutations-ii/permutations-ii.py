class Solution:
    def helper(self,nums,start):
            if start == len(nums):
                return [[]]
            ret = []
            set_int = set()
            for i in range(start, len(nums)):
                if nums[i] not in set_int:
                    nums[start], nums[i] = nums[i], nums[start]
                    perms = self.helper(nums, start + 1)
                    for perm in perms:
                        perm.append(nums[start])
                    ret.extend(perms)
                    nums[start], nums[i] = nums[i], nums[start]
                set_int.add(nums[i])
            return ret
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = self.helper(nums,0)
        # ans = set([tuple(perm) for perm in ans])
        return list(ans)