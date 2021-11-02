class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        def find_root(a):
            while parent[a]!=a:
                a = parent[a]
            return a
        def onecomp(ar):
            ans = 0
            for i in range(len(ar)):
                if ar[i] == i:
                    ans += 1
            return ans == 1
        for edge in edges:
            root1 = find_root(edge[0])
            root2 = find_root(edge[1])
            if root1 == root2:
                return False
            parent[root1] = root2
        return onecomp(parent)
        