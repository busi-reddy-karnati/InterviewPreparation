class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        '''
        rows = len(points)
        cols = len(points[0])
        left and right = [0]*cols
        for i in range(1,rows):
            left[0] = points[i-1][0] This is what we can get.
            right[-1] = points[i-1][-1] This is the maximum we can get
            for j in range(1,cols):
                left[j] = max(left[j-1]-1,points[i-1][j])
                right[-1-j] = max(right[-j]-1,points[i-1][-1-j])
            for j in range(cols):
                points[i][j]+= = max(left[j],right[j])
        return max(points[-1])
        '''
        rows = len(points)
        cols = len(points[0])
        left = [0]*cols
        right = [0]*cols
        for i in range(1,rows):
            left[0] = points[i-1][0]
            right[-1] = points[i-1][-1]
            for j in range(1,cols):
                left[j] = max(left[j-1]-1,points[i-1][j])
                right[-1-j] = max(right[-j]-1,points[i-1][-1-j])
            for j in range(cols):
                points[i][j] += max(left[j],right[j])
        return max(points[-1])