class Solution:
    def rob(self, nums: List[int]) -> int:
        ans_map = {}
        def dp(index):
            
            nonlocal ans_map
            if index >= len(nums):
                return 0
            if index in ans_map:
                return ans_map[index]
            ans = max(nums[index]+dp(index+2), dp(index+1))
            ans_map[index] = ans
            return ans
        return dp(0)
        