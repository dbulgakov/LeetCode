from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        if len(intervals) == 0:
            return res

        intervals.sort(key=lambda x: x[0])

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(0, len(intervals)):
            if start <= intervals[i][0] <= end:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        res.append([start, end])

        return res
