# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, max_allowed, min_allowed):
            if not root:
                return True
            if root.val >= max_allowed or root.val <= min_allowed:
                return False
            return helper(root.left, min(root.val, max_allowed), min_allowed) and helper(root.right, max_allowed, max(min_allowed, root.val))
        return helper(root, float("inf"), float("-inf"))