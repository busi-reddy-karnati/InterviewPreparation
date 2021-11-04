# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def num_nodes(self,root):
        if not root:
            return 0
        return self.num_nodes(root.left)+self.num_nodes(root.right)+1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if self.num_nodes(root.left) >= k:
            return self.kthSmallest(root.left,k)
        else:
            n = self.num_nodes(root.left)
            if n == k-1:
                return root.val
            return self.kthSmallest(root.right,k-(n+1))
        
            