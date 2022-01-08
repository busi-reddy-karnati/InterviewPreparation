class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        pointers = [0 for i in range(rows)]
        while all([pointer<cols for pointer in pointers]):
            flag = 0
            for i in range(rows-1):
                if mat[i][pointers[i]] != mat[i+1][pointers[i+1]]:
                    flag = 1
                    break
            if flag == 0:
                return mat[0][pointers[0]]
            min_index = 0
            min_val = mat[0][pointers[0]]
            for i in range(rows):
                if mat[i][pointers[i]] < min_val:
                    min_index = i
                    min_val = mat[i][pointers[i]]
            pointers[min_index] += 1                
        return -1