# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        number_of_cameras = 0
        def traverse(node):
            nonlocal number_of_cameras
            if not node:
                return 2
            left = traverse(node.left)
            right = traverse(node.right)
            if left == 2 and right == 2:
                #Both of them covered but I am not, So I tell my parent that I am not
                return 1#No camera, not covered
            if left == 1 or right == 1:
                number_of_cameras += 1
                return 3#Camera I have
            if left == 3 or right == 3:
                return 2
        root_val = traverse(root)
        if root_val == 1:
            number_of_cameras += 1
        return number_of_cameras
        