# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_in(self,root,target):
        if root.val == target:
            return True
        cur = root
        while cur.val != target:
            if cur.val > target:
                cur = cur.left
            else:
                cur = cur.right
            if not cur:
                return False
        return True
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val  == p.val or root.val == q.val:
            return root
        p_in_left = self.is_in(root.left,p.val)
        p_in_right = self.is_in(root.right,p.val)
        q_in_left = self.is_in(root.left,q.val)
        q_in_right = self.is_in(root.right,q.val)
        if (p_in_left and q_in_right) or (p_in_right and q_in_left):
            return root
        if p_in_left:
            return self.lowestCommonAncestor(root.left,p,q)
        return self.lowestCommonAncestor(root.right,p,q)