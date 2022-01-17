# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum)
    
    
    def helper(self,root, target):
        if not root:
            return False
        if not root.right and not root.left and target == root.val:
            return True
        if not root:
            return False
        return self.helper(root.left,target-root.val) or self.helper(root.right, target-root.val)
        