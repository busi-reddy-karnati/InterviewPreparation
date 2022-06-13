class Solution:
    def minimumTotal(self, triangle):
        self.dp = {}
        return self.helper(triangle, 0, 0)
    def helper(self,nums,row, col):
        if row >= len(nums):
            return 0
        if (row,col) in self.dp:
            return self.dp[(row,col)]
        ans = nums[row][col] + min(self.helper(nums,row+1,col),self.helper(nums,row+1,col+1))
        self.dp[(row,col)] = ans
        return ans