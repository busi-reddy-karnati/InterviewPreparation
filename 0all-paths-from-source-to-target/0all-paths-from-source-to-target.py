class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        target = len(graph)-1
        ans = []
        def traverse(node, temp_path):
            nonlocal ans
            temp_path.append(node)
            if node == target:
                ans.append([i for i in temp_path])
                temp_path.pop()
                return            
            for neighbour in graph[node]:
                traverse(neighbour, temp_path)
            temp_path.pop()
        traverse(0, [])
        return ans
        