# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def helper(self,root):
        if not root:
            return 0
        right = self.helper(root.right)
        left = self.helper(root.left)
        self.ans+=abs(left-right)
        return root.val+left+right
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.ans
        
    