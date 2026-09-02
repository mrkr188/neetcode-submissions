class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # ALGORITHM STEPS: UNIQUE PATHS (BOTTOM-UP DP)
        #
        # 1. SUBPROBLEMS: Count unique paths from cell (r, c) to target (m-1, n-1)
        # 2. STATE:       dp[r][c] is total unique paths from cell (r, c) to target
        # 3. TRANSITION:  Sum of paths moving right (r, c+1) plus moving down (r+1, c)
        # 4. ITERATION:   Loop row r backwards (m-1 down to 0), col c backwards (n-1 to 0)
        # 5. BASE:        dp[m-1][n-1] = 1 (1 path to stay at destination cell)
        # 6. RESULT:      dp[0][0] represents total unique paths from start to target

        # +1 adds a border of 0s to prevent out-of-bounds errors without needing extra if checks
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # paths from cell (r, c) = paths from cell below + paths from cell right
                #   [r, c]   <--   [r, c + 1] (right)
                #     ^
                #     |
                # [r + 1, c] (below)                
                dp[r][c] += dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]

