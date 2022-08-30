class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        syms = ['*','+','-','/']
        stack = []
        for i in range(len(tokens)):
            char = tokens[i]
            if char in syms:
                match (char):
                    case '+':
                        var1 = stack.pop(-1)
                        var2 = stack.pop(-1)
                        ans = int(var1) + int(var2)
                        stack.append(ans)
                    case '-':
                        var1 = stack.pop(-1)
                        var2 = stack.pop(-1)
                        ans = int(var2) - int(var1)
                        stack.append(ans)
                    case '*':
                        var1 = stack.pop(-1)
                        var2 = stack.pop(-1)
                        ans = int(var1) * int(var2)
                        stack.append(ans)
                    case '/':
                        var1 = stack.pop(-1)
                        var2 = stack.pop(-1)
                        res1 = math.ceil(int(var2)/int(var1))
                        res2 = math.floor(int(var2)/int(var1))
                        if abs(res1-0) < abs(res2-0):
                            ans = res1
                        else:
                            ans = res2
                        stack.append(ans)
            else:
                stack.append(char)
        return stack[-1]
                    