# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        temp_right = root.right
        self.flatten(root.left)
        self.flatten(temp_right)
        root.right = root.left
        temp = root
        while temp.right:
            temp = temp.right
        temp.right = temp_right
        root.left = None