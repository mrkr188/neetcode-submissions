class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda i: i[0])
        
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(intervals[i][1], res[-1][1])
        return res  
        