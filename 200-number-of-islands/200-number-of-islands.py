def clear(grid,row,col):
    if row == len(grid) or col == len(grid[0]) or col == -1 or row == -1:
        return
    if grid[row][col] == "0":
        return
    grid[row][col] = "0"
    clear(grid,row,col+1)
    clear(grid,row+1,col)
    clear(grid,row-1,col)
    clear(grid,row,col-1)
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    ans += 1
                    clear(grid,row,col)
        return ans
    