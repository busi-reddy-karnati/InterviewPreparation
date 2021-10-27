# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        level = [root]
        ans=[]
        while level:
            l = []
            for i in level:
                l.append(i.val)
            ans.append(l)
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        for i in range(len(ans)):
            if i % 2:
                ans[i] = ans[i][::-1]
        return ans
                    
        