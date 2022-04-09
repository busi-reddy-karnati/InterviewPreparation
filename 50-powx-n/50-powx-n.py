class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            return 1/self.myPow(x,-n)
        while n:
            if n%2 == 1:
                ans = ans*x
            x = x*x
            n = n//2
        return ans