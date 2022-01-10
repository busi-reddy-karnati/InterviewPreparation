class Solution:
    def numSplits(self, s: str) -> int:
        start_map = dict(Counter(s))
        end_map = {}
        ans = 0
        for i in range(len(s)):
            if start_map[s[i]] == 1:
                del start_map[s[i]]
            else:
                start_map[s[i]]-=1
            if s[i] in end_map:
                end_map[s[i]]+=1
            else:
                end_map[s[i]]=1
            if len(start_map) == len(end_map):
                ans += 1
        return ans
            
        