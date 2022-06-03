# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #validate(node, min, max)
        return self.validate(root, -((2**31))-2, ((2**31)))
    
    def validate(self, node, mini, maxi):
        if not node:
            return True
        if node.val <= mini or node.val >= maxi:
            return False
        return self.validate(node.left, mini,min(maxi,node.val)) and self.validate(node.right,max(node.val,mini), maxi)