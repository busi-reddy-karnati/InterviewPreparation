class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search(matrix,0,len(matrix)-1,target)
    def search(self, a, start_row, end_row,target):
        if start_row > end_row:
            return False
        mid_row = (start_row+end_row)//2
        mid_col = (len(a[0]))//2
        if a[mid_row][mid_col] == target:
            return True
        elif a[mid_row][mid_col] > target:
            return self.search_col(a,mid_row,0,mid_col-1,target) or self.search(a,start_row,mid_row-1,target)
        else:
            return self.search_col(a,mid_row,mid_col-1,len(a[0])-1,target) or self.search(a,mid_row+1,end_row,target)
    def search_col(self,a, row, start_col, end_col,target):
        while start_col <= end_col:
            mid_col = (start_col+end_col)//2
            if a[row][mid_col] == target:
                return True
            elif a[row][mid_col] > target:
                end_col = mid_col - 1
            else:
                start_col = mid_col + 1
        return False