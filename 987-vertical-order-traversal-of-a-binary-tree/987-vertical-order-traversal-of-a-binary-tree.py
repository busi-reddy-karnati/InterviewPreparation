# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = collections.defaultdict(list)
        queue = collections.deque()
        if not root:
            return []
        queue.append([root,0,0])
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                popped = queue.popleft()
                node = popped[0]
                level = popped[1]
                depth = popped[2]
                levels[(level,depth)].append(node.val)
                if node.left:
                    queue.append([node.left, level-1, depth+1])
                if node.right:
                    queue.append([node.right, level+1, depth+1])
        level_order = collections.defaultdict(list)
        for k in levels:
            elem = levels[k]
            level = k[0]
            elem.sort()
            for node in elem:
                level_order[level].append(node)
        ans = []
        for ke in sorted(level_order):
            ans.append(level_order[ke])
            
        return ans
        