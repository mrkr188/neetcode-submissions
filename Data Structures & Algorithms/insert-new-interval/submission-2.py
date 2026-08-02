class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # newInterval ends before the current interval starts:
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # newInterval starts after the current interval ends
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # newInterval overlaps with current interval - update newInterval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res