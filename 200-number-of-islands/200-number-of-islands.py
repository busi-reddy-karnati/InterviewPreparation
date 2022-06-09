class Solution:
    def clear(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == "1":
            grid[row][col] = "0"
            self.clear(grid,row+1,col)            
            self.clear(grid,row-1,col)
            self.clear(grid,row,col+1)
            self.clear(grid,row,col-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    self.clear(grid, row, col)
                    ans += 1                
        return ans