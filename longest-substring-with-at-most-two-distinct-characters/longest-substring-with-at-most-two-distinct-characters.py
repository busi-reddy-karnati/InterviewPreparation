class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hmap = {}
        ans = 0
        left = 0
        for i,char in enumerate(s):
            # print(i,hmap,sum(hmap.values()))
            if char in hmap:
                hmap[char]+=1
                # print(i,hmap,sum(hmap.values()))
                ans = max(ans,sum(hmap.values()))
            else:
                hmap[char] = 1
                while len(hmap) >2:
                    hmap[s[left]] -= 1
                    if hmap[s[left]] == 0:
                        hmap.pop(s[left])
                    left+=1
                ans = max(ans,sum(hmap.values()))
        return max(ans,sum(hmap.values()))
                    