# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        lis = []
        self.helper(root,targetSum,lis)
        return self.ans
    
    def helper(self, root, targetSum, lis):
        if not root:
            return 
        if not root.left and not root.right and targetSum == root.val:
            lis.append(root.val)
            a = [i for i in lis]
            self.ans.append(a)
            lis.pop(-1)
            return
        lis.append(root.val)
        self.helper(root.left,targetSum-root.val,lis)
        self.helper(root.right,targetSum-root.val,lis)        
        lis.pop(-1)
        
        