from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        opens = {'(','[','{'}
        for char in s:
            if char in opens:
                stack.append(char)
            else:
                if not stack:
                    return False
                elem = stack.pop()
                if elem == '{':
                    if char != '}':
                        return False
                if elem == '[':
                    if char != ']':
                        return False
                if elem == '(':
                    if char != ')':
                        return False
        return not stack
                