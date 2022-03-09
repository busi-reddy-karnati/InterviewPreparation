from heapq import heappush, heappop, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap,num)
            else:
                elem = heap[0]
                if elem < num:
                    heappop(heap)
                    heappush(heap,num)
        return heap[0]
        
        