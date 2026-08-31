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

#                 c = 0               c = 1               c = 2
#             (0 from s2)         (1 from s2)         (2 from s2)
#            +--------------------+--------------------+--------------------+
#  r = 0     |     dp[0][0]       |     dp[0][1]       |     dp[0][2]       |
# (0 from s1)| s3 index: 0 + 0 = 0| s3 index: 0 + 1 = 1| s3 index: 0 + 2 = 2|
#            +--------------------+--------------------+--------------------+
#  r = 1     |     dp[1][0]       |     dp[1][1]       |     dp[1][2]       |
# (1 from s1)| s3 index: 1 + 0 = 1| s3 index: 1 + 1 = 2| s3 index: 1 + 2 = 3|
#            +--------------------+------------------ -+--------------------+
#  r = 2     |     dp[2][0]       |     dp[2][1]       |     dp[2][2]       |
# (2 from s1)| s3 index: 2 + 0 = 2| s3 index: 2 + 1 = 3| BASE CASE = True   |
#            +--------------------+--------------------+--------------------+
#
# evaluated end result for s1 = "ab", s2 = "cd", s3 = "acbd":
#
#                 c = 0               c = 1               c = 2
#             (0 from s2)         (1 from s2)         (2 from s2)
#            +--------------------+-------------------+-------------------+
#  r = 0     |       True         |       False       |       False       |
# (0 from s1)|  s1[0]='a' matches |  cannot form      |  cannot form      |
#            +--------------------+-------------------+-------------------+
#  r = 1     |       True         |       True        |       False       |
# (1 from s1)|  s2[0]='c' matches |  s1[1]='b' matches|  cannot form      |
#            +--------------------+-------------------+-------------------+
#  r = 2     |       False        |       True        |       True        |
# (2 from s1)|  cannot form       |  s2[1]='d' matches|    base case      |
#            +--------------------+-------------------+-------------------+
