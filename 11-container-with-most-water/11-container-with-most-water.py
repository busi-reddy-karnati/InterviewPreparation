class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(height)-1
        ans = 0
        while pointer1 < pointer2:
            ans = max(ans,(pointer2-pointer1)*min(height[pointer1],height[pointer2]))
            if height[pointer1] < height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1
        return ans
        