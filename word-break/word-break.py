class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        dp = {}
        def helper(indx):
            # print(indx)
            nonlocal dp
            if indx in dp:
                return dp[indx]
            if indx >= len(s):
                return True
            for word in words:
                if s[indx:].startswith(word):
                    if helper(indx+len(word)):
                        dp[indx] = True
                        return True
            dp[indx] = False
            return False
        return helper(0)