class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(index):
            nonlocal ans_map
            if index in ans_map:
                return ans_map[index]
            if index >= len(nums):
                return 0
            ans = max(dp(index+1), dp(index+2)+nums[index])
            ans_map[index] = ans
            return ans
        ans_map = {}
        return dp(0)