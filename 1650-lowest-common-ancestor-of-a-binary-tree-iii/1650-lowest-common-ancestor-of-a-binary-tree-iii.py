"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def path_len(node):
            if not node:
                return 0
            ans = 0
            while node.parent:
                node = node.parent
                ans += 1
            return ans
        p_len = path_len(p)
        q_len = path_len(q)
        if p_len < q_len:
            for i in range(abs(p_len-q_len)):
                q = q.parent
        else:
            for i in range(abs(q_len-p_len)):
                p = p.parent
        while p!=q:
            p = p.parent
            q = q.parent
        return p