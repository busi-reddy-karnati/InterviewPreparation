# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.height = self.height(root)
        return self.helper(root,1)
    def helper(self, root, level):
        if not root:
            return 0
        if level == self.height:
            return root.val
        return self.helper(root.left, level+1)+self.helper(root.right, level+1)
    