from collections import defaultdict
class Solution:
    dic = defaultdict(list)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = defaultdict(list)
        self.helper(root)
        x = sorted(self.dic)
        ans = []
        for i in x:
            ans.append(self.dic[i])
        return ans
    def helper(self, root):
        if not root:
            return
        queue = []
        queue.append((root,0))
        while queue:
            top = queue.pop(0)
            node = top[0]
            ind = top[1]
            self.dic[ind].append(node.val)
            if node.left:
                queue.append((node.left,ind-1))
            if node.right:
                queue.append((node.right,ind+1))
        