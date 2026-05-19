class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        if not matrix:
            return []
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()
        
        for r in range(num_rows):
            for c in range(num_cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        for r in zero_rows:
            for c in range(num_cols):
                matrix[r][c] = 0
        
        for c in zero_cols:
            for r in range(num_rows):
                matrix[r][c] = 0



