from heapq import heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap,num)
                continue
            if heap[0] < num:
                heappop(heap)
                heappush(heap,num)
        return heap[0]