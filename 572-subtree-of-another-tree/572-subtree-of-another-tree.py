# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        return self.inorder(root,subRoot)
    
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return root.val == subRoot.val and self.sameTree(root.left,subRoot.left) and self.sameTree(root.right, subRoot.right)
    
    def inorder(self, root, subRoot):
        if not root:
            return False
        if root.val == subRoot.val:
            if self.sameTree(root,subRoot):
                return True
        return self.inorder(root.left,subRoot) or self.inorder(root.right,subRoot)
    
            