class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x,y):
            nonlocal grid
            if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
                return
            if grid[x][y] == "0":
                return
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            grid[x][y] = "0"
            for direction in directions:
                x_new = x + direction[0]
                y_new = y + direction[1]
                bfs(x_new, y_new)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    bfs(i,j)
        return ans