class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hmap = collections.defaultdict(int)
        for interval in intervals:
            hmap[interval[0]] += 1
            hmap[interval[1]] -= 1
        hmap = sorted(hmap.items(),key=operator.itemgetter(0))
        ans = 0
        tempans = 0
        for elem in hmap:
            tempans += elem[1]
            ans = max(ans,tempans)
        return ans