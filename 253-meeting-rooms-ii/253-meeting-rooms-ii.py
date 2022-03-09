class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ln = 0
        for interval in intervals:
            ln = max(ln,interval[1])
            # print(interval[1])
        ln+=1
        meetings_timeline = [0]*ln
        for interval in intervals:
            meetings_timeline[interval[0]] += 1
            meetings_timeline[interval[1]] -= 1
        ans = 0
        meetings = 0
        for i in range(ln):
            meetings += meetings_timeline[i]
            ans = max(ans,meetings)
        return ans
        