from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2==1:return []
        changed.sort()
        ans = []
        hmap = defaultdict(int)
        for num in changed:
            hmap[num]+=1
        hmap = dict(sorted(hmap.items()))
        # print(hmap)
        for num in hmap:
            if num == 0:
                if hmap[num]%2:
                    return []
                for i in range(hmap[num]//2):
                    ans.append(num)
                continue
            if hmap[num] == 0:
                continue
            if hmap[num] > 0 and 2*num in hmap and hmap[2*num] >= hmap[num]:
                for i in range(hmap[num]):
                    ans.append(num)
                hmap[2*num]-=hmap[num]
                hmap[num] = 0
            else:
                return []
        return ans
        