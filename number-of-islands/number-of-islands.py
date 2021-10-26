class Solution:
    def clear_land(self,grid,x,y):
        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):
            return
        if grid[x][y] == "1":
            grid[x][y] = "-1"
            for i  in [1,-1]:
                self.clear_land(grid,x,y+i)
                self.clear_land(grid,x+i,y)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    self.clear_land(grid,i,j)
        return ans
        