class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        mod = 1000000007
        for i in range(1,n+1):
            p = len(bin(i))-2
            p = 2**p
            ans = (((ans*p)%mod)+(i))%mod
        return ans
    