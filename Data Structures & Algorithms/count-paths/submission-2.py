class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

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

