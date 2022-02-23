"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited ={}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        if node in self.visited:
            return self.visited[node]
        neighbour_list = []
        new_node = Node(node.val,neighbour_list)
        self.visited[node] = new_node 
        for neighbour in node.neighbors:
            neighbour_list.append(self.cloneGraph(neighbour))
        
        return new_node
        