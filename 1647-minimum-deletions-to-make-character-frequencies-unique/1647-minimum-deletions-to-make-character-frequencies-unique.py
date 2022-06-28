class Solution:
    def minDeletions(self, s: str) -> int:
        sc = Counter(s)
        l = list(sc.values())
        l.sort(reverse = True)
        print(l)
        ans = 0
        for i in range(1,len(l)):
            if l[i-1] == 0:
                ans += l[i]
                l[i] = 0
            elif l[i] >= l[i-1]:#Less than is important. Let's say 2,1,2 when we come to 2, it means we decremented 2 to 1
                ans += l[i]-l[i-1]+1
                l[i] = l[i-1]-1
        return ans