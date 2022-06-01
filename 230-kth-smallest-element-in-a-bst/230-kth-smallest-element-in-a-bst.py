
def numElemsInTree(root):
    if not root:
        return 0
    return 1+numElemsInTree(root.left)+numElemsInTree(root.right)
class Solution:
    def kthSmallest(self, root, k):
        left_count = numElemsInTree(root.left)
        if left_count == k-1:
            return root.val
        if left_count >= k:
            return self.kthSmallest(root.left,k)
        else:
            return self.kthSmallest(root.right, k-left_count-1)
        