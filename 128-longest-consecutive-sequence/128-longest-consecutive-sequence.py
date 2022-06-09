class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for num in numSet:
            if num-1 not in numSet:
                temp = num
                while temp in numSet:
                    temp += 1
                ans = max(ans,temp-num)
        return ans
        