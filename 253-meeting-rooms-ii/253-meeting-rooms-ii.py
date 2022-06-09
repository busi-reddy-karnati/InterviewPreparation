class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts =  [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]
        starts.sort()
        ends.sort()
        tempRooms = 0
        startPtr = 0
        endPtr = 0
        ans = 0
        while startPtr < len(intervals):
            if starts[startPtr] == ends[endPtr]:
                startPtr += 1
                endPtr += 1
            elif starts[startPtr] < ends[endPtr]:
                tempRooms += 1
                startPtr+=1
            else:
                tempRooms-=1
                endPtr+=1
            ans = max(ans,tempRooms)
        return ans