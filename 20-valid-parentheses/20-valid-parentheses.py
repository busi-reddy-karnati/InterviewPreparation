from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opens = {'(', '[','{'}
        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == '}' and stack.pop() != '{':
                    return False
                if char == ']' and stack.pop() != '[':
                    return False
                if char == ')' and stack.pop() != '(':
                    return False
        return not stack
                
        