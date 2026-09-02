class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:


        # ALGORITHM STEPS: LONGEST COMMON SUBSEQUENCE (BOTTOM-UP DP)
        #
        # 1. SUBPROBLEMS: Find length of LCS for suffixes text1[i:] and text2[j:]
        # 2. STATE:       dp[i][j] is max LCS length for suffixes text1[i:] and text2[j:]
        # 3. TRANSITION:  If characters match:
        #                     Add 1 to length and advance both pointers (i+1, j+1)
        #                 If characters differ:
        #                     Take max of skipping text1 char (i+1) vs text2 char (j+1)
        # 4. ITERATION:   Loop i backwards (len1 down to 0), j backwards (len2 down to 0)
        # 5. BASE:        dp[len1][j] = dp[i][len2] = 0 (empty suffix yields 0 length)
        # 6. RESULT:      dp[0][0] is length of LCS for full text1 and full text2

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