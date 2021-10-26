# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def is_celebrity(self,person,n):
        for guest in range(n):
            if person != guest:
                if not knows(guest,person):
                    return False
                if knows(person,guest):
                    return False
        return True
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            if self.is_celebrity(i,n):
                return i
        return -1