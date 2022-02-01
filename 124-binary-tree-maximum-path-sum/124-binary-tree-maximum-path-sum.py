# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        p = self.helper(root)
        return self.ans
    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        # print(left,right,root.val)
        self.ans = max(self.ans,left+right+root.val,left+root.val,right+root.val,root.val)
        if max(left,right) < 0:
            return root.val
        return max(left,right)+root.val
    