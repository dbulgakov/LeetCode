class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort()

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        for i in intervals[1:]:
            left = max(i[0], prev_start)
            right = min(i[1], prev_end)

            if left < right:
                return False

            prev_start = i[0]
            prev_end = i[1]

        return True
