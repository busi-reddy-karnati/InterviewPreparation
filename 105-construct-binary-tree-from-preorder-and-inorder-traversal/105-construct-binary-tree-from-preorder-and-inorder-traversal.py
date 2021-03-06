# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def binary_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
            
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)<1:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        val = preorder[0]
        root = TreeNode(val)
        index = binary_search(inorder, val)
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
        