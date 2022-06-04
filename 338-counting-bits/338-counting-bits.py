class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            return [0,1,1]
        ans = [0,1,1]
        for i in range(3, n+1):
            if i%2==0:
                ans.append(ans[i//2])
            else:
                ans.append(ans[i//2]+1)
        return ans