class Solution:
    ans = []
    def helper(self, digits, inde, aux):
        digit_map = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['i','h','g'],
            '5':['j','k','l'],
            '6':['o','n','m'],
            '7':['p','q','r','s'],
            '8':['v','u','t'],
            '9':['w','x','y','z'],            
        }
        
        if inde >= len(digits):
            self.ans.append("".join(aux))
            return
        for char in digit_map[digits[inde]]:
            aux.append(char)
            self.helper(digits, inde+1,aux)
            aux.pop(-1)
        
        
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.ans = []
        self.helper(digits,0,[])
        return self.ans
        