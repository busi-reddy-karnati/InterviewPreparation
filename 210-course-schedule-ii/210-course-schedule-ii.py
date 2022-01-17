from collections import defaultdict
class Solution:
    status = {}
    children = {}
    ans_stack = []
    def cycle(self, node):
        # return True
        self.status[node] = 1
        stack = [node]
        while stack:
            flag = 0
            for child in self.children[stack[-1]]:
                if self.status[child] == 1:
                    return True
                if self.status[child] == 0:
                    stack.append(child)
                    self.status[child] = 1
                    flag = 1
                    break
            if flag == 0:
                self.status[stack.pop(-1)] = 2
        return False
       
    def visit(self, node):
        for child in self.children[node]:
            if self.status[child] == 0:
                self.status[child] = 1
                self.visit(child)
        self.ans_stack.append(node)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.status = {}
        self.ans_stack = []
        self.children = defaultdict(list)
        for prereq in prerequisites:
            self.children[prereq[0]].append(prereq[1])
        # print(self.children)
        for i in range(numCourses):
            self.status[i] = 0
        for i in range(numCourses):
            if self.status[i] == 0:
                if self.cycle(i):
                    return []
        self.status = {}
        for i in range(numCourses):
            self.status[i] = 0
        for i in range(numCourses):
            if self.status[i] == 0:
                self.status[i] = 1
                self.visit(i)
        return self.ans_stack