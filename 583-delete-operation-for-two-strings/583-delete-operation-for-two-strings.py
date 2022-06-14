class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        n = len(word1)
        m = len(word2)
        for i in range(n+1):
            dp.append([0 for i in range(m+1)])
        for i in range(1,n+1):
            for j in range(1,m+1):
                p1 = i-1
                p2 = j-1
                if word1[p1] == word2[p2]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return len(word1)+len(word2)-2*dp[n][m]