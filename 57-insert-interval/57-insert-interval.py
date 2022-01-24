class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        lo = 0
        hi = len(intervals)-1
        ind = -1
        while hi >= lo:
            
            mid = (hi+lo)//2
            # print(intervals[mid][0],newInterval[0])
            if intervals[mid][0] >= newInterval[0]:
                print("he")
                ind = mid
                hi = mid-1
            else:
                lo = mid+1
        if ind == -1:
            intervals.append(newInterval)
        else:
            intervals.insert(ind,newInterval)
        # print(intervals)
        ans = []
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(intervals[i][1],ans[-1][1])
            else:
                ans.append(intervals[i])
        return ans
            