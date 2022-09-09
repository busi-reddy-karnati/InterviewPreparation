class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            nonlocal grid
            nonlocal area
            nonlocal ans
            if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
                return
            if grid[x][y] == 0:
                return 
            grid[x][y] = 0
            area += 1
            # print(x,y,area)
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for direction in directions:
                # print(x,y," -> calling ->",end=" ")
                x_new = x+direction[0]
                y_new = y + direction[1]
                # print(x_new,y_new)
                bfs(x_new,y_new)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    bfs(i,j)
                    # print(i,j, area)
                    ans = max(ans, area)
        return ans
                    