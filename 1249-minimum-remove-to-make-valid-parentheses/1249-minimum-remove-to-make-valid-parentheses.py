class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        l = list(s)
        for i,char in enumerate(s):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    l[i] = ""
                else:
                    stack.pop(-1)
        
        for ind in stack:
            l[ind] = ""
        return "".join(l)