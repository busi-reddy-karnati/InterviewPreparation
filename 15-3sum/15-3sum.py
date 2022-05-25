class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p = []
        n = []
        zs = 0
        for num in nums:
            if num < 0 :
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                zs += 1
        ans = set()
        if zs > 2:
            ans.add((0,0,0))
        ps = set(p)
        ns = set(n)
        if zs > 0:
            for num in ps:
                if -num in ns:
                    ans.add((-num,0,num))
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -(p[i]+p[j])
                if target in ns:
                    ans.add(tuple(sorted((p[i],p[j],target))))
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -(n[i]+n[j])
                if target in ps:
                    ans.add(tuple(sorted((n[i],n[j],target))))
        return [list(i) for i in ans]
    
                