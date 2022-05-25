class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(0,i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # print(matrix) success transpose
        for i in range(n):
            for j in range(int(n/2)):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
        