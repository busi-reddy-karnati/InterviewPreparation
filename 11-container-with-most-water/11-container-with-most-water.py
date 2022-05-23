class Solution:
    def maxArea(self, height):
        n = len(height)
        ans = 0
        right = n-1
        left = 0
        while left < right:
            ans = max(min(height[left],height[right])*(right-left),ans)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans