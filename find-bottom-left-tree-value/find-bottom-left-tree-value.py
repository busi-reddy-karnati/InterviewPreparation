# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_level = 0
    ans = 0
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.helper(root,1)
        return self.ans
    def helper(self,root,level):
        if not root:
            return
        if level > self.max_level:
            self.max_level = level
            self.ans = root.val
        self.helper(root.left,level+1)
        self.helper(root.right,level+1)