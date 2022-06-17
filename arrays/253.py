class Solution:
    # Time: O(n log n)
    # Space: O(n)

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start_times = sorted([x[0] for x in intervals])
        end_times = sorted([x[1] for x in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start_times[s] < end_times[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            res = max(res, count)

        return res