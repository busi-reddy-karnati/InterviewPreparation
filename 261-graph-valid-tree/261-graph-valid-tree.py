def getRoot(parent, node):
    while parent[node] != node:
        node = parent[node]
    return node

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = {}
        for i in range(n):
            parent[i] = i
        for edge in edges:
            rootX = getRoot(parent,edge[0])
            rootY = getRoot(parent,edge[1])
            if rootX == rootY:
                return False#checks for cycle condition
            parent[rootX] = rootY
        numComps = 0
        for i in range(n):
            if parent[i] == i:
                numComps += 1
        return numComps == 1
        