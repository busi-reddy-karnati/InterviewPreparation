class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = []
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            ans_end = ans[-1][1]
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= ans_end:
                ans[-1][1] = max(ans_end,end)
            else:
                ans.append([start,end])
        return ans