# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth_order = collections.defaultdict(list)
        def traverse_depth(node):
            nonlocal depth_order
            if not node:
                return -1
            left_depth = traverse_depth(node.left)
            right_depth = traverse_depth(node.right)
            depth = max(left_depth, right_depth)+1
            depth_order[depth].append(node.val)
            return depth
        ans = []
        traverse_depth(root)
        # print(depth_order)
        for ke in sorted(depth_order):
            ans.append(depth_order[ke])
        return ans