class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        res = [[1], [1,1]]
        
        row = [1,1]
        
        for i in range(2, numRows):
            row = [1] + [x+y for x,y in zip(row, row[1:])] + [1]
            res.append(row)
        
        return res