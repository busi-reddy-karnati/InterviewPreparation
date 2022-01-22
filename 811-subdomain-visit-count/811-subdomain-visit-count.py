from collections import defaultdict
class Solution:
    def subdomainVisits(self, domains: List[str]) -> List[str]:
        ans_map = defaultdict(int)
        for x in domains:
            count,domain = x.split(" ")
            domain = domain.split(".")
            for i in range(len(domain)):
                ans_map[".".join(domain[i:])]+=int(count)
        ans = []
        for k,v in ans_map.items():
            ans.append(str(v)+" "+str(k))
        return ans