# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def helper(root):
            if not root:
                return 0
            nonlocal ans
            left = helper(root.left)
            right = helper(root.right)
            
            #update answer
            ans = max(ans, root.val+left, root.val+right, root.val+left+right, root.val)
            #return max of (me)+(optional left or right)
            return max(root.val, root.val+left, root.val+right)
        helper(root)
        return ans