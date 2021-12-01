# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hmap = {}
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.hmap={}
        self.helper(root,1)
        return list(self.hmap.values())
    def helper(self,root,level):
        if not root:
            return
        self.hmap[level] = root.val
        self.helper(root.left,level+1)
        self.helper(root.right,level+1)