from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = deque()
        for i,char in enumerate(list(s)):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack or s[stack[-1]] == ')':
                    # print(i)
                    stack.append(i)
                else:
                    stack.pop()
        ans = []
        ind_stack = 0
        # print(stack)
        for i in range(len(s)):
            if ind_stack < len(stack) and stack[ind_stack] == i:
                ind_stack += 1
            else:
                ans.append(s[i])
        return "".join(ans)
        