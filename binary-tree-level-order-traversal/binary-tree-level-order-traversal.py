# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        present_level = [root]
        if not root:
            return []
        while present_level:
            ans.append([i.val for i in present_level])
            next_level = []
            for node in present_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            present_level = next_level
        return ans
        