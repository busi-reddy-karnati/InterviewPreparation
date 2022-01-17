from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        hmap = defaultdict(int)
        hmap[fruits[0]]+=1
        p1 = 0
        p2 = 1
        ans = 0
        while p2 < len(fruits):
            hmap[fruits[p2]]+=1
            while len(hmap) > 2:
                hmap[fruits[p1]]-=1
                if hmap[fruits[p1]] == 0:
                    del hmap[fruits[p1]]
                p1+=1
            ans = max(ans,sum(hmap.values()))
            p2+=1
        
        return ans
        