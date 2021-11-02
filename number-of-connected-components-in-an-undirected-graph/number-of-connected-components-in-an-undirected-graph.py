class Solution:
    parents = []
    def get_root(self,index):
        while self.parents[index]!=index:
            index = self.parents[index]
        return index

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parents = [i for i in range(n)]
        for edge in edges:
            root1 = self.get_root(edge[0])
            root2 = self.get_root(edge[1])
            if root1 != root2:
                self.parents[root1] = root2
        ans = 0
        for i in range(n):
            if self.parents[i] == i:
                ans += 1
        return ans
        