class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        children = {}
        for i in range(n):
            children[i] = []
        for pre in prerequisites:
            children[pre[1]].append(pre[0])
        for i in range(n):
            stack = [i]
            visited = {}
            for j in range(n):
                visited[j] = 0
            visited[i] = 1
            while stack:
                node = stack[-1]
                childs = children[node]
                flag = 0
                for child in childs:
                    if visited[child] == 1:
                        return False
                    if visited[child]==0:
                        stack.append(child)
                        visited[child] = 1
                        flag = 1
                        break
                if flag == 0:
                    node = stack.pop(-1)
                    visited[node] = 2
        return True