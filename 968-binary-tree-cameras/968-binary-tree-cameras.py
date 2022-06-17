# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def dfs(self, root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l == 1 or r == 1:
            self.count+=1
            return 2
        if l==2 or r == 2:
            return 0
        return 1
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        if self.dfs(root) == 1:
            self.count += 1
        return self.count        