# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
def do_dfs(root, ans):
    if not root:
        return 0
    ret = 1+max(do_dfs(root.left,ans),do_dfs(root.right,ans))
    ans[ret].append(root.val)
    return ret
class Solution:
    
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        x = do_dfs(root,ans)
        a = ans.values()
        return (list(a))
        