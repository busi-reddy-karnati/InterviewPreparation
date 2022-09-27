# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, end: int) -> str:
        #2 find the path from LCA to start
            #2.1 reverse the path that is there
            #If I generate L(Left), R(Right) Then i Can replace with that length of parents
        #3 find path from LSA to end
        def find_path(node, target):
            nonlocal trace_path
            if not node:
                return False
            if node.val == target:
                return True
            left = find_path(node.left, target)
            if left:
                trace_path.appendleft("L")
                return True
            right = find_path(node.right, target)
            if right:
                trace_path.appendleft("R")
                return True
        def find_lca(node):
            if not node:
                return
            if node.val == start:
                return node
            if node.val == end:
                return node
            left = find_lca(node.left)
            right = find_lca(node.right)
            if left and right:
                return node
            return left or right
        lca = find_lca(root)
        trace_path = collections.deque()
        find_path(lca, start)
        ans = "U"*len(trace_path)
        trace_path = collections.deque()
        find_path(lca, end)
        
        ans = ans + "".join(trace_path)
        return ans
        