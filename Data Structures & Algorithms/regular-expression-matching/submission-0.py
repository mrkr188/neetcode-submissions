class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # approach: bottom-up dp matching suffixes of string s and pattern p.
        # dp[r][c] = true if suffix s[r:] matches pattern suffix p[c:].
        #
        # evaluated grid for s = "aa", p = "a*":
        #
        #                 c = 0        c = 1        c = 2
        #                  ('a')        ('*')       (empty)
        #               +------------+------------+------------+
        #  r = 0 ('a')  |    True    |   False    |   False    |
        #               +------------+------------+------------+
        #  r = 1 ('a')  |    True    |   False    |   False    |
        #               +------------+------------+------------+
        #  r = 2 (emp)  |    True    |   False    |    True    |
        #               +------------+------------+------------+

        rows, cols = len(s), len(p)
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]

        # base case: empty string matches empty pattern
        dp[rows][cols] = True

        # fill table backwards from suffixes down to prefixes
        for r in range(rows, -1, -1):
            for c in range(cols - 1, -1, -1):

                # check if current characters match or pattern has dot wildcard
                match = r < rows and (s[r] == p[c] or p[c] == '.')

                # handle '*' wildcard: skip 2 pattern chars or consume 1 char in s
                if (c + 1) < cols and p[c + 1] == '*':
                    dp[r][c] = dp[r][c + 2]
                    if match:
                        dp[r][c] = dp[r + 1][c] or dp[r][c]
                # single char match: advance both pointers
                elif match:
                    dp[r][c] = dp[r + 1][c + 1]

        # returns whether full string s[0:] matches full pattern p[0:]
        return dp[0][0]

