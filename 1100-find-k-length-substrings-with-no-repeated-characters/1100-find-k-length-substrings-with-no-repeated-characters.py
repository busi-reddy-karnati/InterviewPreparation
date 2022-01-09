class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return 0
        hmap = {}
        ans = 0
        for i in range(k):
            if s[i] in hmap:
                hmap[s[i]]+=1
            else:
                hmap[s[i]] = 1
        if len(hmap) == k:
            ans += 1
        for i in range(1,n-k+1):
            if hmap[s[i-1]] == 1:
                del hmap[s[i-1]]
            else:
                hmap[s[i-1]]-=1
            if s[i+k-1] in hmap:
                hmap[s[i+k-1]]+=1
            else:
                hmap[s[i+k-1]] = 1
            if len(hmap) == k:
                ans += 1
        return ans
        