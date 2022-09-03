# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, max_val):
            if not node:
                return 0
            left_good_nodes = helper(node.left, max(max_val, node.val))
            right_good_nodes = helper(node.right, max(max_val, node.val))
            adde = 0
            if node.val >= max_val:
                adde = 1
            return adde + left_good_nodes + right_good_nodes
        return helper(root, float("-inf"))