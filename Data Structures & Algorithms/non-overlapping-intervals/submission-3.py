class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev = 0

        # when intervals don't overlap we move forward assigning prev = i
        # if intervals overlap there's two cases
        # 1. when interval at i falls completely within prev interval, 
        #    then we discard bigger interval at prev and append 1 to count 
        #    and assign prev = i
        # 2. when interval at i overlaps interval at prev but end of i is less 
        #    than end of prev interval, then we add q to count and keep prev = prev

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                if intervals[i][1] < intervals[prev][1]:
                    prev = i
                count += 1
            else:
                prev = i
        return count
