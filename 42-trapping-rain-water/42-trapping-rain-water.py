class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height)-1
        left_max,right_max  = height[left],height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max,height[left])
                ans += -height[left]+left_max
            else:
                right -= 1
                right_max = max(right_max, height[right])
                ans += -height[right]+right_max
        return ans