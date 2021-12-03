class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dp={}
        return self.helper(grid,0,0)
    def helper(self,grid,i,j):
        key = str(i)+" "+str(j)
        if key in self.dp:
            return self.dp[key]
        if i == len(grid)-1 and j == len(grid[0])-1:
            return grid[i][j]
        if i == len(grid)-1:
            ans = grid[i][j]+self.helper(grid,i,j+1)
            self.dp[key] = ans
            return ans
        
        if j == len(grid[0])-1:
            ans = grid[i][j]+self.helper(grid,i+1,j)
            self.dp[key] = ans
            return ans
        ans = min(grid[i][j]+self.helper(grid,i,j+1),grid[i][j]+self.helper(grid,i+1,j))
        self.dp[key] = ans
        return ans