class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        max_water_stored = 0
        water_stored = 0
        right = len(height)-1
        while left <= right:
            water_stored = min(height[left], height[right])*(right-left)
            max_water_stored = max(water_stored, max_water_stored)
            #update the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water_stored