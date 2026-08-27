class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res += 4
                    if c and grid[r][c-1]:
                        res -= 2
                    if r and grid[r-1][c]:
                        res -= 2
        return res


        