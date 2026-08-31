class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)

        # dp[row][col] means: lcs of text1[row:] and text2[col:]
        dp = [[0 for col in range(n + 1)] for row in range(m + 1)]

        # iterate backwards from bottom-right corner
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                # characters match: add 1 and move diagonally
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                # characters differ: take best option skipping current char in text1 or text2
                else:
                    dp[row][col] = max(dp[row][col + 1], dp[row + 1][col])

        # dp[0][0] stores lcs length for full strings text1[0:] and text2[0:]
        return dp[0][0]

#
# evaluated grid for text1 = "abc", text2 = "ace":
#
#                 col = 0        col = 1        col = 2        col = 3
#                  ('a')          ('c')          ('e')         (empty)
#               +--------------+--------------+--------------+--------------+
#  row = 0 ('a')|      2       |      1       |      0       |      0       |
#               +--------------+--------------+--------------+--------------+
#  row = 1 ('b')|      1       |      1       |      0       |      0       |
#               +--------------+--------------+--------------+--------------+
#  row = 2 ('c')|      1       |      1       |      0       |      0       |
#               +--------------+--------------+--------------+--------------+
#  row = 3 (emp)|      0       |      0       |      0       |      0       |
#               +--------------+--------------+--------------+--------------+