from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        if rows == cols == 1:
            return 0
        queue.append((0,0,k,0))#Format is x, y, obstacles_remaining, steps_taken
        visited = set()
        visited.add((0,0,k))
        cords_change = [[-1,0],[1,0],[0,1],[0,-1]]
        while queue:
            node = queue.popleft()
            x = node[0]
            y = node[1]
            obstacles_remaining = node[2]
            steps = node[3]
            if x == rows-1 and y == cols-1:
                return steps
            steps += 1
            if grid[x][y] == 1:
                obstacles_remaining -= 1
            if obstacles_remaining < 0:
                continue
            for coord in cords_change:
                new_x = x+coord[0]
                new_y = y+coord[1]
                if 0<=new_x<rows and 0<=new_y<cols and (new_x,new_y,obstacles_remaining) not in visited:
                    visited.add((new_x,new_y,obstacles_remaining))
                    queue.append((new_x,new_y,obstacles_remaining,steps))
        return -1
            
        