class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        # open, close, aux
        self.helper(0,0,[],n)
        return self.ans
    def helper(self, opens, closes, aux, n):
        if opens == closes and closes == n:
            s = "".join(aux)
            self.ans.append(s)
            return
        half = int(n)
        '''
        open: opens<n/2
        close: opens > close
        
        '''
        if opens < half:
            aux.append('(')
            self.helper(opens+1, closes, aux, n)
            aux.pop()
        if closes < opens:
            aux.append(')')
            self.helper(opens,closes+1,aux,n)
            aux.pop()
        
            