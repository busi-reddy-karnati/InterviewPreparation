# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_val = root.val
        return self.is_good(root,max_val)
    def is_good(self, root, max_val):
        if not root:
            return 0
        if root.val >= max_val:
            return 1+self.is_good(root.left,max(max_val,root.val))+self.is_good(root.right,max(max_val,root.val))
        return self.is_good(root.left,max(max_val,root.val))+self.is_good(root.right,max(max_val,root.val))
        