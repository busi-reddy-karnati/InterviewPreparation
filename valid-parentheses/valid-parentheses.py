class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ['(','[','{']
        open_map = {'[':']','{':'}','(':')'}
        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack[-1]
                stack.pop()
                if open_map[top] != char:
                    return False
        return not stack