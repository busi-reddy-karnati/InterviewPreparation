from collections import defaultdict
class Solution:
    def subarraySum(self, arr: List[int], target: int) -> int:
        running_sums = defaultdict(int)
        running_sums[0] = 1
        ans = 0
        temp_sum = 0
        for i in range(len(arr)):
            temp_sum += arr[i]
            ans+=running_sums[temp_sum-target]
            running_sums[temp_sum]+=1
        return ans