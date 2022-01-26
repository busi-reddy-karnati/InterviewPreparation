from collections import deque
class Solution:
    hmap = {}
    def minKnightMoves(self, x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        if x+y == 1:
            return 3
        if x == 1 and y == 1:
            return 2
        
        if x+y == 0:
            return 0
        key = (x,y)
        if key in self.hmap:
            return self.hmap[key]
        ans = 1+min(self.minKnightMoves(abs(x-1),abs(y-2)),self.minKnightMoves(abs(x-2),abs(y-1)))
        self.hmap[key] = ans
        return ans