class Solution:
    def helper(self, str1, str2):
        ans = ""
        smallLen = min(len(str1),len(str2))
        for i in range(smallLen):
            if str1[i] != str2[i]:
                return ans
            ans += str1[i]
        return ans
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1,len(strs)):
            ans = self.helper(ans,strs[i])
        return ans