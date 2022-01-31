from heapq import heappush,heappop,heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)
        while len(stones)>1:
            stone1 = abs(heappop(stones))
            stone2 = abs(heappop(stones))
            if abs(stone1-stone2) > 0:
                heappush(stones,-(abs(stone1-stone2)))
        if stones:
            return abs(stones[0])
        return 0
        
        