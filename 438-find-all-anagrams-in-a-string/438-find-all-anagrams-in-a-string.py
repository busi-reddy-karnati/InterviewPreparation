from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, t: str) -> List[int]:
        n1 = len(s)
        n2 = len(t)
        if n1<n2:
            return []
        hmap1 = defaultdict(int)
        hmap2 = defaultdict(int)
        ans = []
        for i in range(n2):
            hmap1[s[i]]+=1
            hmap2[t[i]]+=1
        if hmap1 == hmap2:
            ans.append(0)
        for i in range(n1-n2):
            if hmap1[s[i]] == 1:
                del hmap1[s[i]]
            else:
                hmap1[s[i]]-=1
            hmap1[s[i+n2]]+=1
            if hmap1 == hmap2:
                ans.append(i+1)
        return ans