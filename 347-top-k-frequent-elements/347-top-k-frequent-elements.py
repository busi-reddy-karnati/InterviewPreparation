from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            freq = hmap.get(num,0)
            hmap[num] = freq + 1
        heap = []
        for i in hmap:
            freq = hmap[i]
            if len(heap) < k:
                heappush(heap, freq)
            else:
                if heap[0] < freq:
                    heappop(heap)
                    heappush(heap, freq)
        threshold = heap[0]
        ans = []
        for num in hmap:
            if hmap[num] >= threshold:
                ans.append(num) 
        return ans