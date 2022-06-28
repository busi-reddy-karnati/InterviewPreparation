class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source = image[sr][sc]
        target = color
        self.visited = set()
        self.helper(image, source, target, sr, sc)
        return image
    def helper(self, nums, source, target, row, col):
        if row < 0 or row >= len(nums):
            return
        if col < 0 or col >= len(nums[0]):
            return 
        if nums[row][col] != source:
            return
        if (row,col) in self.visited:
            return
        nums[row][col] = target
        self.visited.add((row,col))
        self.helper(nums,source,target,row+1,col)
        self.helper(nums,source,target,row,col+1)        
        self.helper(nums,source,target,row-1,col)        
        self.helper(nums,source,target,row,col-1)        