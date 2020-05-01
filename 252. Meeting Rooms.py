class Solution:
    def canAttendMeetings(self, intervals):
        Start = []
        End = []
        for i in intervals:
            Start.append(i[0])
            End.append(i[1])

        Start.sort()
        End.sort()

        for i in range(len(Start) - 1):
            if Start[i + 1] <= End[i]:
                return False
        return True
