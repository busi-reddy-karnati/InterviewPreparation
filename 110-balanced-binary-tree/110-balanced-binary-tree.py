# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.traverse(root)
        return self.ans
    def traverse(self, root):
        if not root:
            return 0
        left_height = self.traverse(root.left)
        right_height = self.traverse(root.right)
        if abs(left_height-right_height) > 1:
            self.ans = False
        return max(left_height, right_height)+1
    