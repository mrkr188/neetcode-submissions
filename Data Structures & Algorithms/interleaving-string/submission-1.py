class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        rows, cols = len(s1), len(s2)
        if len(s3) != rows + cols:
            return False

        # dp grid where dp[r][c] means s1[r:] and s2[c:] can form s3[r+c:]
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]

        # base case: empty suffixes match empty target
        dp[rows][cols] = True

        # iterate bottom-up from bottom-right corner
        for r in range(rows, -1, -1):
            for c in range(cols, -1, -1):
                # match current character of s3 with s1
                if r < rows and s3[r + c] == s1[r] and dp[r + 1][c]:
                    dp[r][c] = True
                # match current character of s3 with s2
                if c < cols and s3[r + c] == s2[c] and dp[r][c + 1]:
                    dp[r][c] = True

        return dp[0][0]
