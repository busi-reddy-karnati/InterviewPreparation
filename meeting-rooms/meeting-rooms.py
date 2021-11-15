class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = list(sorted(intervals,key = operator.itemgetter(0)))
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
        