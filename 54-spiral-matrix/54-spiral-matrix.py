class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def isValid(a,b):
            return 0<=a and a<len(matrix) and 0<=b and b<len(matrix[0]) and matrix[a][b]>-100
        directions = [0,1]
        ans = []
        x = 0
        y = 0
        
        while len(ans) != len(matrix)*len(matrix[0]):
            ans.append(matrix[x][y])
            matrix[x][y] = -200
            if not isValid(x+directions[0],y+directions[1]):
                if directions[0] == 0 and directions[1] == 1:
                    directions[0] =1
                    directions[1] = 0
                elif directions[0]==1 and directions[1]==0:
                    directions[0] = 0
                    directions[1] = -1
                elif directions[0] == 0 and directions[1] == -1:
                    directions[0] = -1
                    directions[1] = 0
                else:
                    directions[0] = 0
                    directions[1] = 1
            x = x+directions[0]
            y = y+directions[1]
        return ans