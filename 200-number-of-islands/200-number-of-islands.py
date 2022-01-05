def modify_grid(grid, x, y):
    if x < 0 or x > len(grid)-1:
        return
    if y < 0 or y > len(grid[0])-1:
        return
    if grid[x][y] == "0":
        return
    grid[x][y] = "0"
    modify_grid(grid,x+1,y)
    modify_grid(grid,x,y+1)
    modify_grid(grid,x-1,y)
    modify_grid(grid,x,y-1)
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)        
        cols = len(grid[0])
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    ans += 1
                    modify_grid(grid,i,j)
                    
        return ans