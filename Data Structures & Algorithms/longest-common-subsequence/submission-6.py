class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)

        # initialize dp grid with extra row/col for empty base cases
        dp = [[0 for row in range(n + 1)] for col in range(m + 1)]

        # iterate backwards from bottom-right corner
        for col in range(m - 1, -1, -1):
            for row in range(n - 1, -1, -1):
                # characters match: add 1 and move diagonally
                if text1[col] == text2[row]:
                    dp[col][row] = 1 + dp[col + 1][row + 1]
                # characters differ: take best option skipping current char in text1 or text2
                else:
                    dp[col][row] = max(dp[col][row + 1], dp[col + 1][row])

        # dp[0][0] stores lcs length for full strings text1[0:] and text2[0:]
        return dp[0][0]

# dp[col][row] means: lcs of text1[col:] and text2[row:]
#
# evaluated grid for text1 = "abc", text2 = "ace":
#
#                 row = 0        row = 1        row = 2        row = 3
#                  ('a')          ('c')          ('e')         (empty)
#               +--------------+--------------+--------------+--------------+
#  col = 0 ('a')|      2       |      1       |      0       |      0       |
#               +--------------+--------------+--------------+--------------+
#  col = 1 ('b')|      1       |      1       |      0       |      0       |
#               +--------------+--------------+--------------+--------------+
#  col = 2 ('c')|      1       |      1       |      0       |      0       |
#               +--------------+--------------+--------------+--------------+
#  col = 3 (emp)|      0       |      0       |      0       |      0       |
#               +--------------+--------------+--------------+--------------+