class Solution:
    def get_root(self,n):
        while self.parent[n] != n:
            n = self.parent[n]
        return n
    def union(self, a, b):
        root1 = self.get_root(a)
        root2 = self.get_root(b)
        if root1 != root2:
            self.parent[root1] = root2
        
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        self.parent = [i for i in range(n)]
        for edge in edges:
            self.union(edge[0],edge[1])
        return self.get_root(start) == self.get_root(end)
        