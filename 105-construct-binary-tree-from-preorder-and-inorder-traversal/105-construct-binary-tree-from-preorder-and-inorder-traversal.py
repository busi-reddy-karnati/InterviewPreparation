# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            nonlocal preorder_index
            if right < left:
                return
            val = preorder[preorder_index]
            preorder_index += 1
            index = inorder_index[val]
            root = TreeNode(val)
            root.left = helper(left, index-1)
            root.right = helper(index+1, right)
            return root
        preorder_index = 0
        inorder_index = {}
        for i, num in enumerate(inorder):
            inorder_index[num] = i
        return helper(0, len(preorder)-1)
    