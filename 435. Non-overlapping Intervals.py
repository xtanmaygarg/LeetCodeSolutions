class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda Start: Start[0])
        Count = 0
        End = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < End:
                Count += 1
                End = min(intervals[i][1], End)
            else:
                End = intervals[i][1]
        return Count
