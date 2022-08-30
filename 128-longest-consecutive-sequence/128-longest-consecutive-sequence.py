class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        if not nums:
            return 0
        for num in nums:
            hashset.add(num)
        ans = 1
        for num in hashset:
            if num-1 not in hashset:
                temp = num
                seq_len = 1
                while temp+1 in hashset:
                    temp = temp+1
                    seq_len += 1
                ans = max(ans,seq_len)
        return ans