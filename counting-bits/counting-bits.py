class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        power = 1
        for i in range(1,len(ans)):
            if i == power*2:
                power = power*2
            ans[i] = ans[i-power]+1
        return ans
        