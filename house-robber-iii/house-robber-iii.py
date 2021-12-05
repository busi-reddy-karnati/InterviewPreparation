# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hmap = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root in self.hmap:
            return self.hmap[root]
        if not root.left and not root.right:
            ans = root.val
            self.hmap[root] = ans
            return ans
        children = self.rob(root.left)+self.rob(root.right)
        grand_children = 0
        if root.left:
            grand_children += self.rob(root.left.left)+self.rob(root.left.right)
        if root.right:
            grand_children += self.rob(root.right.left)+self.rob(root.right.right)
        ans = max(root.val+grand_children,children)
        self.hmap[root] = ans
        return ans
    