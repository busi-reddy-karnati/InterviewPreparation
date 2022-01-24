# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def evaluate(root):
    if root.val != '+':
        return root.val
    return evaluate(root.left)+evaluate(root.right)

class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        e1 = list(evaluate(root1))
        e2 = list(evaluate(root2))
        e1.sort()
        e2.sort()
        return e1 == e2 