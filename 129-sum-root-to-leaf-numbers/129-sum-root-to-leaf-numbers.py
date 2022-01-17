# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,0)
    def helper(self,root,ans):
        if not root:
            return 0
        ret = ans*10+root.val
        if not root.right and not root.left:
            return ret
        return self.helper(root.left,ret)+self.helper(root.right,ret)
    
        