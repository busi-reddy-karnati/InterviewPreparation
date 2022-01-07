class Solution:
    def isArmstrong(self, n: int) -> bool:
        po = len(str(n))
        square_sum = 0
        temp_n = n
        while n:
            digit = n%10
            n = n//10
            # print(digit**po)
            square_sum+=digit**po
        # print(square_sum,n)
        return square_sum == temp_n
        