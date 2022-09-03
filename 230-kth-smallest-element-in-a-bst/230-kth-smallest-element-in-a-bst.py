# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    inorder = []
    def traverse(self, node):
        if not node:
            return 
        self.traverse(node.left)
        self.inorder.append(node.val)
        self.traverse(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder = []
        self.traverse(root)
        return self.inorder[k-1]