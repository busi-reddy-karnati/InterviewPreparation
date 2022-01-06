class Solution:
    def visit(self,nestedList, depth):
        res = 0
        for item in nestedList:
            if item.isInteger():
                res += item.getInteger()*depth
            else:
                res += self.visit(item.getList(), depth+1)
        return res
    def depthSum(self, nestedList):
        return self.visit(nestedList, 1)