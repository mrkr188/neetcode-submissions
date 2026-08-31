class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ROWS, COLS = len(s), len(t)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS+1):
            dp[r][COLS] = 1
        
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                dp[r][c] = dp[r+1][c]
                if s[r] == t[c]:
                    dp[r][c] += dp[r+1][c+1]
        
        return dp[0][0]

        # if len(t) > len(s):
        #     return 0

        # # i is index of s, j is index of t
        # # (i, j) -> count of distinct subsequences
        # dp = {} 

        # # top-down dfs with memoization counts ways to match t[j:] within s[i:]
        # # when chars match, we sum choices to match or skip s[i]; if not, we must skip s[i]
        # def dfs(i, j):

        #     # if we reach end of t, we have count 1
        #     if j == len(t):
        #         return 1
        #     # when we reach end of s, count is 0 since we didn't find any match
        #     if i == len(s):
        #         return 0
            
        #     if (i, j) in dp:
        #         return dp[(i, j)]
            
        #     if s[i] == t[j]:
        #         dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
        #     else:
        #         dp[(i, j)] = dfs(i + 1, j)
            
        #     return dp[(i, j)]
        
        # return dfs(0, 0)
        