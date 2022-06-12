class Solution:
    dp = {}
    def numDecodings(self, s: str) -> int:
        if s in self.dp:
            return self.dp[s]
        if not s:
            return 1
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        if s[0] == '1' or (s[0] == '2' and int(s[1]) <= 6):
            ans = self.numDecodings(s[1:])+self.numDecodings(s[2:])
            self.dp[s] = ans
            return ans
        ans = self.numDecodings(s[1:])
        self.dp[s] = ans
        return ans