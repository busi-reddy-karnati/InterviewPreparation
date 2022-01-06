class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        members = [0]*1001
        for trip in trips:
            num = trip[0]
            start = trip[1]
            end = trip[2]
            members[start]+=num
            members[end] -=num
        for i in range(1001):
            if capacity < members[i]:
                return False
            capacity = capacity-members[i]
        return True
        