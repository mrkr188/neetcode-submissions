class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # +1 adds a border of 0s to prevent out-of-bounds errors without needing extra if checks
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]

