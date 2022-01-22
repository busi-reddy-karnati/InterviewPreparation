class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        if not intervals:
            return intervals
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            flag = 0
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1],end)
            else:
                ans.append(intervals[i])
        return ans
                
        