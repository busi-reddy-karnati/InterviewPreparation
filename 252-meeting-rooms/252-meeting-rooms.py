class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if not intervals:
            return True
        max_time = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < max_time:
                return False
            max_time = max(intervals[i][1],max_time)
        return True