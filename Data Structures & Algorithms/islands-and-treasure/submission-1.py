class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r,c])
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r+x, c+y
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append([nr, nc])

            