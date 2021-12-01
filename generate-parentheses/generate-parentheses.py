class Solution:
    ans = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.helper(n,0,0,"")
        return self.ans
    def helper(self,n,op,cl,s):
        if op == cl == n:
            self.ans.append(s)
            
        if op < n:
            self.helper(n,op+1,cl,s+"(")
        if op > cl:
            self.helper(n,op,cl+1,s+")")
            
            