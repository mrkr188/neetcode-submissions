class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or r > ROWS-1 or c < 0 or c > COLS-1 or 
                (r,c) in visited or prevHeight > heights[r][c]):
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, -math.inf)
            dfs(ROWS-1, c, atl, -math.inf)
    
        for r in range(ROWS):
            dfs(r, 0, pac, -math.inf)
            dfs(r, COLS-1, atl, -math.inf)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res


