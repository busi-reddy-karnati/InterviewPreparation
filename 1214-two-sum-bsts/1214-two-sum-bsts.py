# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree_to_list(self, root, l):
        if not root:
            return l
        l = self.tree_to_list(root.left,l)
        l.append(root.val)
        l = self.tree_to_list(root.right, l)
        return l
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        arr1 = self.tree_to_list(root1,[])
        arr2 = self.tree_to_list(root2,[])
        p1 = 0
        p2 = len(arr2)-1
        while p1 < len(arr1) and p2 >= 0:
            sum = arr1[p1]+arr2[p2]
            if sum == target:
                return True
            if sum > target:
                p2-=1
            else:
                p1+=1
        return False

        
        