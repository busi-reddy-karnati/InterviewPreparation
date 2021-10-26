class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = operator.itemgetter(0))
        ans = [intervals[0]]
        last = -1
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if ans[last][1] < interval[0]:
                ans.append(interval)
            else:
                ans[last][1] = max(interval[1],ans[last][1])
        return ans
        