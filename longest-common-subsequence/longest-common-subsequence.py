class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        s1 = s1[::-1]
        s2 = s2[::-1]
        n1 = len(s1)
        n2 = len(s2)
        a = []
        for i in range(n1):
            a.append([0]*n2)
        if s1[0] == s2[0]:
            a[0][0] = 1
        for i in range(1,n2):
            if s1[0] == s2[i]:
                a[0][i] =1
            else:
                a[0][i] = a[0][i-1]
        for i in range(1,n1):
            if s1[i] == s2[0]:
                a[i][0] = 1
            else:
                a[i][0] = a[i-1][0]
        for i in range(1,n1):
            for j in range(1,n2):
                if s1[i]==s2[j]:
                    a[i][j] = 1+a[i-1][j-1]
                else:
                    a[i][j] = max(a[i-1][j],a[i][j-1])
        return a[n1-1][n2-1]