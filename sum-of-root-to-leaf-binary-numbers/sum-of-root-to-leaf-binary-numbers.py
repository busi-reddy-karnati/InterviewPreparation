# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
    def helper(self, root, val):
        if not root:
            return 0
        if not root.left and not root.right:
            return val*2+root.val
        ans = self.helper(root.left, val*2 + root.val)+self.helper(root.right,val*2+root.val)
        # print(ans)
        return ans
    