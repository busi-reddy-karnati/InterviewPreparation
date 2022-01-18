# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    num_nodes_seen = 0
    ans = 0
    def helper(self,root,k):
        if not root:
            return
        self.helper(root.left,k)
        self.num_nodes_seen += 1
        if self.num_nodes_seen == k:
            self.ans = root.val
        self.helper(root.right,k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.num_nodes_seen = 0
        self.helper(root,k)
        return self.ans