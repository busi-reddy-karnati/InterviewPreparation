class Solution:
    def is_perfect_square(self,n):
        return int(math.sqrt(n))*int(math.sqrt(n)) == n
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        ar=[0]*(n+1)
        ar[0] = 1
        ar[1] = 1
        ar[2] = 2
        for i in range(3,n+1):
            if self.is_perfect_square(i):
                ar[i] = 1
                continue
            col = i
            # print("col  {}".format(i))
            for j in range(1,int(math.sqrt(i))+1):
                # print(j,i-(j*j))
                # print(1+ar[i-(j*j)])
                # print(col,1+ar[i-(j*j)])
                col = min(col,1+ar[i-(j*j)])
            ar[i] = col
        print(ar)
        return ar[n]