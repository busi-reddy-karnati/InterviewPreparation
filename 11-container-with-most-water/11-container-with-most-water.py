class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = 0
        while left < right:
            water_stored = min(height[left], height[right])*(right-left)
            if water_stored > ans:
                ans = water_stored
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return ans