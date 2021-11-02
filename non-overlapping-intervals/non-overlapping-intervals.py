class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = float('-inf')
        removed = 0
        for interval in sorted(intervals,key=lambda x:x[1]):
            if interval[0]<end:
                removed += 1
            else:
                end = interval[1]
        return removed
        