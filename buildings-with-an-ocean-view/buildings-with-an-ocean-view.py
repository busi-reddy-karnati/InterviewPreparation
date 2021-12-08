class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        heights = heights[::-1]
        maxh = 0
        ans = []
        n = len(heights)
        for i in range(len(heights)):
            if heights[i] > maxh:
                ans.append(n-i-1)
                maxh = heights[i]
        return ans[::-1]
        