class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        
        def visit(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            nonlocal visited
            if grid[i][j] == "0" or (i,j) in visited:
                return
            
            directions = [[-1,0],[0,-1],[0,1],[1,0]]
            visited.add((i,j))
            for direction in directions:
                new_x = i + direction[0]
                new_y = j + direction[1]
                visit(new_x,new_y)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans += 1
                    visit(i,j)
        return ans