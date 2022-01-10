class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        ans = -1
        for num in nums:
            if num>ans and hmap[num]==1:
                ans = num
        return ans