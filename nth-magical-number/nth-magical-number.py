class Solution:
    def gcd(self,a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mini = 1
        maxi = max(a,b)*n
        while mini<maxi:
            mid = (mini+maxi)//2
            numdiv = mid // a + mid // b - mid // ((a * b) // gcd(a, b))
            if numdiv < n:
                mini = mid+1
            else:
                maxi = mid
        return mini%1000000007
                
            
        