class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # ALGORITHM STEPS: DISTINCT SUBSEQUENCES (BOTTOM-UP DP)
        #
        # 1. SUBPROBLEMS: Count ways suffix s[i:] can form target suffix t[j:]
        # 2. STATE:       dp[i][j] is total distinct ways s[i:] forms t[j:]
        # 3. TRANSITION:  If characters match:
        #                     Sum of using s[i] (advance both) plus skipping
        #                     s[i] to find other matches (advance s pointer)
        #                 If characters differ:
        #                     Skip s[i] to find matches in remainder (advance s)
        # 4. ITERATION:   Loop i backwards (len_s to 0), j backwards (len_t to 0)
        # 5. BASE:        An empty target string t can always be formed in 1 way
        # 6. RESULT:      dp[0][0] is distinct ways full string s forms full string t
        #
        # evaluated grid for s = "rabb", t = "rab":
        #
        #                    c = 0        c = 1        c = 2        c = 3
        #                    ('r')        ('a')        ('b')       (empty)
        #                 +------------+------------+------------+------------+
        #  r = 0 ('r')    |     2      |     2      |     2      |     1      |
        #                 +------------+------------+------------+------------+
        #  r = 1 ('a')    |     0      |     2      |     2      |     1      |
        #                 +------------+------------+------------+------------+
        #  r = 2 ('b')    |     0      |     0      |     2      |     1      |
        #                 +------------+------------+------------+------------+
        #  r = 3 ('b')    |     0      |     0      |     1      |     1      |
        #                 +------------+------------+------------+------------+
        #  r = 4 (empty)  |     0      |     0      |     0      |     1      |
        #                 +------------+------------+------------+------------+

        rows, cols = len(s), len(t)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # base case: an empty string t (cols) can be formed 1 way from any suffix of s
        for r in range(rows + 1):
            dp[r][cols] = 1

        # fill table backwards starting from bottom-right
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                # choice 1: skip current character in s
                dp[r][c] = dp[r + 1][c]
                # choice 2: match characters, add paths that match both s[r] and t[c]
                if s[r] == t[c]:
                    dp[r][c] += dp[r + 1][c + 1]

        # answer for full strings s[0:] and t[0:]
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
        