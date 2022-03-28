class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        BF: have a hashtable with rows and cols as entries
        if an element is 0, makes its corresponding row and col as true
        for each element, see if the corresponding row or col are true, if so set 0. Else 1
        
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        zz = matrix[0][0] == 0
        zr = False
        zc = False
        for i in range(cols):
            if matrix[0][i] == 0:
                zr = True
        for i in range(rows):
            if matrix[i][0] == 0:
                zc = True
        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[0][col] == 0 or matrix[row][0]==0:
                    matrix[row][col] = 0
        if zz:
            for row in range(rows):
                matrix[row][0] = 0
            for col in range(cols):
                matrix[0][col] = 0
        else:
            if zr:
                for i in range(cols):
                    matrix[0][i] = 0
            if zc:
                for i in range(rows):
                    matrix[i][0] = 0
                    