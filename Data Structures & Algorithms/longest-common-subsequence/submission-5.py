class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m, n = len(text1), len(text2)
        dp = [[0 for row in range(n+ 1)] for col in range(m + 1)]

        for col in range(m - 1, -1, -1):
            for row in range(n - 1, -1, -1):
                if text1[col] == text2[row]:
                    dp[col][row] = 1 + dp[col + 1][row + 1]
                else:
                    dp[col][row] = max(dp[col][row + 1], dp[col + 1][row])

        return dp[0][0]

