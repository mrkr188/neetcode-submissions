class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # ALGORITHM STEPS: LONGEST INCREASING PATH IN A MATRIX (MEMOIZED DP)
        #
        # 1. SUBPROBLEMS: Find longest increasing path starting from cell (r, c)
        # 2. STATE:       dp[r][c] is max path length starting at grid cell (r, c)
        # 3. TRANSITION:  For all adjacent neighbors with strictly greater values:
        #                     Path length is 1 + max path length among those neighbors
        #                 If no greater neighbor exists:
        #                     Path length is 1 (the cell itself)
        # 4. ITERATION:   Top-down DFS with memoization, computed on demand per cell
        # 5. BASE:        Unvisited cells compute via neighbors; visited return dp[r][c]
        # 6. RESULT:      Maximum value found across all dp[r][c] entries in grid
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} # (r, c) -> longest increasing path (lip)

        # dfs reaches biggest numbers first, then smaller numbers build on their results
        # strictly increasing values prevent loops, allowing us to safely cache each cell's answer
        def dfs(r, c, prevVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                res = max(res, 1 + dfs(r+x, c+y, matrix[r][c]))
            
            dp[(r, c)] = res
            return res
        
        res = 1
        for r in range(ROWS):
            for c in range(COLS):
                res = max(dfs(r, c, -1), res)
        return res

