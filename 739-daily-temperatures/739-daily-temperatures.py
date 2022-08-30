class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temps)
        for i,temp in enumerate(temps):
            while stack and temp > temps[stack[-1]]:
                ans[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return ans