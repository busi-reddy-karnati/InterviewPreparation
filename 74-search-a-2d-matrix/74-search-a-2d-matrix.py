class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = (m*n)-1
        while low <= high:
            mid = (low+high)//2
            x = mid // n
            y = mid % n
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                high = mid -1
            else:
                low = mid + 1
        return False