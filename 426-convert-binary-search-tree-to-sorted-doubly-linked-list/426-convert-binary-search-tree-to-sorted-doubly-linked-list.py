"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def helper_inorder(self, root):
        if not root:
            return
        self.helper_inorder(root.left)
        node = Node(root.val)
        node.left = self.tail
        self.tail.right = node
        self.tail = self.tail.right
        self.helper_inorder(root.right)
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        self.head = Node(0)
        self.tail = self.head
        self.helper_inorder(root)
        self.head = self.head.right
        self.head.left = self.tail
        self.tail.right = self.head
        return self.head
        
        