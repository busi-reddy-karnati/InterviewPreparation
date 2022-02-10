# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_path = []
        self.q_path = []
        self.dfs(root,p,q,[])
        while self.p_path and self.q_path:
            pointer = 0
            while pointer < len(self.p_path) and pointer <len(self.q_path) and self.p_path[pointer] == self.q_path[pointer]:
                pointer += 1
            return self.p_path[pointer-1]
        return 
    def dfs(self, root, p, q,path):
        if not root:
            return
        if root == p:
            self.p_path = [node for node in path]
            self.p_path.append(root)
        if root == q:
            self.q_path = [node for node in path]
            self.q_path.append(root)
        path.append(root)
        self.dfs(root.left,p,q,path)
        self.dfs(root.right,p,q,path)
        path.pop(-1)
            
		

