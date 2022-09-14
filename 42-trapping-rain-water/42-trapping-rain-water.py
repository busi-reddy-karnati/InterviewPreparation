class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftmax = height[left]
        rightmax = height[right]
        ans = 0
        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(height[left], leftmax)
                if height[left] < leftmax:
                    ans += leftmax-height[left]
            else:
                right -= 1
                rightmax = max(height[right], rightmax)
                if height[right] < rightmax:
                    ans += rightmax-height[right]
        return ans