"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        children = []
        for child in root.children:
            children.append(self.cloneTree(child))
        new_root = Node(root.val, children)
        return new_root