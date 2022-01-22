from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_set = defaultdict(int)
        sum_set[0] = 1
        ans = 0
        temp_sum = 0
        for num in nums:
            temp_sum += num
            ans += sum_set[temp_sum-k]
            sum_set[temp_sum]+=1
        return ans