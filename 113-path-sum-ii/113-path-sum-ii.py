# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def traverse(node, temp_list, sum_here):
            nonlocal ans
            if not node.right and not node.left:
                if sum_here == targetSum:
                    ans.append([i for i in temp_list])
                return
            if node.left:
                temp_list.append(node.left.val)
                traverse(node.left, temp_list, sum_here+node.left.val)
                temp_list.pop()
            if node.right:
                temp_list.append(node.right.val)
                traverse(node.right, temp_list, sum_here+node.right.val)
                temp_list.pop()
            
        if not root:
            return []
        traverse(root,[root.val],root.val)
        return ans