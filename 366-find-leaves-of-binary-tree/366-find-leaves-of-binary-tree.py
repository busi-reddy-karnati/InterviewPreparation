# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def helper(self, root):
        if not root:
            return 0
        level = 1+max(self.helper(root.left), self.helper(root.right))
        self.hmap[level].append(root.val)
        return level
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.hmap = defaultdict(list)
        self.helper(root)
        keys = sorted(self.hmap)
        ans = []
        for key in keys:
            ans.append(self.hmap[key])
        return ans