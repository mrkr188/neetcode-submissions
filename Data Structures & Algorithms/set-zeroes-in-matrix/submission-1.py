class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        if not matrix:
            return []

        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        

        
        # num_rows = len(matrix)
        # num_cols = len(matrix[0])
        # zero_rows = set()
        # zero_cols = set()
        
        # for r in range(num_rows):
        #     for c in range(num_cols):
        #         if matrix[r][c] == 0:
        #             zero_rows.add(r)
        #             zero_cols.add(c)
        
        # for r in zero_rows:
        #     for c in range(num_cols):
        #         matrix[r][c] = 0
        
        # for c in zero_cols:
        #     for r in range(num_rows):
        #         matrix[r][c] = 0



