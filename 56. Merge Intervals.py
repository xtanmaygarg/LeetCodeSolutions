class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda Slot: Slot[0])
        Output = []
        Output.append(intervals[0])
        Start = intervals[0][0]
        End = intervals[0][1]
        for i in range(1, len(intervals)):
            if End >= intervals[i][0]:
                Output.pop()
                End = max(End, intervals[i][1])
                Output.append([Start, End])
            else:
                Output.append(intervals[i])
                Start = intervals[i][0]
                End = intervals[i][1]
        return Output
