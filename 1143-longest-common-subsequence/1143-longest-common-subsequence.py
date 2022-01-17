class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.dp = {}
        return self.longest_common_subsequence_brute_force(text1, text2, 0,0)
    def longest_common_subsequence_brute_force(self,s1, s2, p1, p2):
        key = str(p1)+" "+str(p2)
        if key in self.dp:
            return self.dp[key]
        if p1 == len(s1) or p2 == len(s2):
            return 0
        if s1[p1] == s2[p2]:
            ans = 1+self.longest_common_subsequence_brute_force(s1,s2,p1+1,p2+1)
            self.dp[key] = ans
            return ans
        else:
            ans = max(self.longest_common_subsequence_brute_force(s1,s2,p1,p2+1),self.longest_common_subsequence_brute_force(s1,s2,p1+1,p2))
            self.dp[key] = ans
            return ans
