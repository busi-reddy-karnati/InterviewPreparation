# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    inorder = []
    def inorderTraversal(self,root):
        if not root:
            return
        self.inorderTraversal(root.left)
        self.inorder.append(root.val)
        self.inorderTraversal(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder = []
        self.inorderTraversal(root)
        return self.inorder[k-1]
        