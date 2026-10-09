class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1:
                return
            if grid[r][c] == '1':
                grid[r][c] = '0'
                for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    dfs(r+x, c+y)
        
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count

        # ROWS, COLS = len(grid), len(grid[0])
        # def bfs(start):
        #     queue = deque([start])
        #     while queue:
        #         r, c = queue.popleft()
        #         if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1:
        #             continue
        #         if grid[r][c] == '1':
        #             grid[r][c] = '0'
        #             for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
        #                 queue.append([r+x, c+y])
        
        # count = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == '1':
        #             count += 1
        #             bfs([r,c])
        # return count



