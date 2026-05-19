class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        num_rows, num_cols = len(matrix), len(matrix[0])
        l, r = 0, num_rows*num_cols
        while l < r:
            m = l + (r-l)//2
            row, col = m//num_cols, m%num_cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m
            else:
                l = m+1
        return False
        