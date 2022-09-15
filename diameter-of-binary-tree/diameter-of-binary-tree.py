# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return 0
            
            left_path = helper(node.left)
            right_path = helper(node.right)
            ans = max(left_path+right_path, ans)
            return max(left_path,right_path)+1
        helper(root)
        return ans