from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
    def pop(self):
        elem = self.stack.pop()
        return elem
    def push(self,elem):
        self.stack.append(elem)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = Stack()
        num = 0
        s = list(s)
        for i in range(len(s)):
            char = s[i]
            if char.isnumeric():
                num = num*10+int(char)
            elif char == '[':
                stack.push(num)
                num = 0
            elif char == ']':
                temp_str = []
                elem = stack.pop()
                while not isinstance(elem,int):
                    temp_str.append(elem)
                    elem = stack.pop()
                string = "".join(temp_str[::-1])
                temp_list = []
                for i in range(elem):
                    temp_list.append(string)
                stack.push("".join(temp_list))
            else:
                stack.push(char)
        return "".join(stack.stack)