# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical_order = collections.defaultdict(list)
        q = collections.deque()
        if not root:
            return []
        q.append([root,0])
        while q:
            qlen = len(q)
            for i in range(qlen):
                popped = q.popleft()
                node = popped[0]
                level = popped[1]
                if node.left:
                    q.append([node.left, level-1])
                if node.right:
                    q.append([node.right, level+1])
                vertical_order[level].append(node.val)
        ans= []
        
        for ke in sorted(vertical_order):
            ans.append(vertical_order[ke])
        return ans
        