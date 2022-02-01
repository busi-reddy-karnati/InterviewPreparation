from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = list(s)
        stack = deque()
        stack.append(-1)
        ans = 0
        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans,i-stack[-1])
        return ans