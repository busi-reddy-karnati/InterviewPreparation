class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],-x[1]))
        answer = []
        answer.append(intervals[0])
        for i in range(1,len(intervals)):
            prev = answer[-1]
            interval = intervals[i]
            if not(prev[0]<=interval[0]<=prev[1] and prev[0]<=interval[1]<=prev[1]):
                answer.append(interval)
                
        return len(answer)