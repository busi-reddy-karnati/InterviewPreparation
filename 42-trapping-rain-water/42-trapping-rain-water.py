class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        max_right[-1] = 0
        max_left[0] = 0
        n = len(height)
        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i-1])
            # print(n-i-1)
            ind = n-i-1
            max_right[n-i-1] = max(max_right[ind+1],height[ind+1])
        ans = 0
        for i in range(n):
            elem = min(max_right[i],max_left[i])
            if elem > height[i]:
                ans += elem-height[i]
        return ans