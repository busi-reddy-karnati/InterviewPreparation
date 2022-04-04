class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        '''
        Questions: 
        Is this a square matrix?
        What are the constrains?
        possible range of values in the matrix?
        
        brute force:
        start going by column by column and inserting into the new matrix
        complexity: time:n^2
                    space:n^2
        
        better?
        do a transpose and a mirror image(inplace possible)
        complexity: time:n^2
                    space: 1
        
        '''
        #Transpose
        n = len(a)
        for i in range(n):
            for j in range(i):
                a[i][j], a[j][i] = a[j][i],a[i][j]
        
        #done transpose - working
            
        
        #mirror
        for i in range(n):
            for j in range(n//2):
                ind = j
                swap_ind = n-j-1
                a[i][ind],a[i][swap_ind] = a[i][swap_ind],a[i][ind]
            
        