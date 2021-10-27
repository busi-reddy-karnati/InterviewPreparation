class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            row = matrix.pop(0)  
            for num in row:
                ans.append(num)
            temp = []
            if len(matrix) == 0:
                return ans
            for i in range(len(matrix[0])):
                ar = []
                for j in range(len(matrix)):
                    ar.append(matrix[j][i])
                temp.append(ar)
            
            matrix = []
            for i in temp:
                matrix.append(i)
            matrix.reverse()
        
            
        return ans
        