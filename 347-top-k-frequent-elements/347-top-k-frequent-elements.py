class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        count_array = [[] for i in range(len(nums)+1)]
        for num in freq:
            count_array[freq[num]].append(num)
        res = []
        for i in range(len(count_array)-1,0,-1):
            for num in count_array[i]:
                res.append(num)
            if len(res) == k:
                return res