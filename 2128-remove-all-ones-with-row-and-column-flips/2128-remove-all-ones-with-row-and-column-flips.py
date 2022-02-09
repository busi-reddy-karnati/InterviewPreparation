class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        row_odd_set = set()
        col_odd_set = set()
        row_even_set = set()
        col_even_set = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    if row in row_even_set and col in col_odd_set:
                        return False
                    if row in row_odd_set and col in col_even_set:
                        return False
                    if row in row_even_set or col in col_even_set:
                        row_even_set.add(row)
                        col_even_set.add(col)
                    else:
                        row_odd_set.add(row)
                        col_odd_set.add(col)                    
                else:
                    if row in row_even_set and col in col_even_set:
                        return False
                    if row in row_odd_set and col in col_odd_set:
                        return False
                    if row in row_even_set or col in col_odd_set:
                        row_even_set.add(row)
                        col_odd_set.add(col)
                    else:
                        row_odd_set.add(row)
                        col_even_set.add(col)   
        return True