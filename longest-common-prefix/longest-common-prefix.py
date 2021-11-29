class Solution:
    def find(self,s1,s2):
        n = min(len(s1),len(s2))
        ans = []
        for i in range(n):
            if s1[i]!=s2[i]:
                return "".join(ans)
            ans.append(s1[i])
        return "".join(ans)
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        ans = strs[0]
        for i in range(1,len(strs)):
            ans = self.find(ans,strs[i])
        return ans