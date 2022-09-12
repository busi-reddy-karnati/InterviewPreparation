class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # in place transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        '''
        1 2    1 3
        3 4    2 4
        '''
        n = len(matrix)
        # mirroring about the middle col
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
        