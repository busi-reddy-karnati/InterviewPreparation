class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        answer = []
        answer.append(intervals[0])
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]            
            if start <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1],end)
            else:
                answer.append(intervals[i])
        return answer