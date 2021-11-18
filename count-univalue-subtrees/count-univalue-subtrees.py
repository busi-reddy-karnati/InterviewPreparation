# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if self.helper(root):
            return 1+self.countUnivalSubtrees(root.left)+self.countUnivalSubtrees(root.right)
        else:
            return self.countUnivalSubtrees(root.left)+self.countUnivalSubtrees(root.right)
        
    def helper(self,root):
        if not root:
            return True
        if root.left:
            if root.left.val != root.val:
                return False
        if root.right:
            if root.right.val != root.val:
                return False
        return self.helper(root.left) and self.helper(root.right)