class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # ALGORITHM STEPS: REGULAR EXPRESSION MATCHING (BOTTOM-UP DP)
        #
        # 1. SUBPROBLEMS: Check if suffix s[r:] matches pattern suffix p[c:]
        # 2. STATE:       dp[r][c] is True if suffix s[r:] matches pattern suffix p[c:]
        # 3. TRANSITION:  If star pattern (e.g. 'a*'):
        #                     Skip 'x*' pair OR consume 1 char in s if characters match
        #                 If standard character (no star):
        #                     Match current character directly and advance both pointers
        # 4. ITERATION:   Loop backwards from end to start (bottom-right to top-left)
        # 5. BASE:        dp[ROWS][COLS] = True because empty string matches empty pattern
        # 6. RESULT:      dp[0][0] represents full string s[0:] matching full pattern p[0:]

        ROWS, COLS = len(s), len(p)
        dp = [[False] * (COLS + 1) for _ in range(ROWS + 1)]

        # base case: empty string matches empty pattern
        dp[ROWS][COLS] = True

        # r starts at ROWS because empty string s[ROWS:] can match patterns like "a*"
        for r in range(ROWS, -1, -1):
            # c starts at COLS - 1 because empty pattern p[COLS:] can never match non-empty s
            # we also check with p[c], which will fail if we start at COLS (p's max index is COLS-1)
            for c in range(COLS - 1, -1, -1):

                # check if next character in pattern is '*' wildcard
                has_star = (c + 1) < COLS and p[c + 1] == '*'
                # check if current single characters match (or pattern has '.' wildcard)
                match = r < ROWS and (s[r] == p[c] or p[c] == '.')

                if has_star:
                    # option 1: skip '*' pattern pair (use 0 times) -> dp[r][c + 2]
                    # option 2: if matched, consume 1 char in s and keep '*' -> dp[r + 1][c]
                    dp[r][c] = dp[r][c + 2]
                    if match:
                        dp[r][c] = dp[r][c] or dp[r + 1][c]
                    # this can be made into 1 line using 
                    # dp[r][c] = dp[r][c + 2] or (match and dp[r + 1][c])
                elif match:
                    # standard match: advance both string and pattern pointers
                    dp[r][c] = dp[r + 1][c + 1]

        # answer for full string s[0:] and full pattern p[0:]
        return dp[0][0]

        # evaluated grid for s = "aa", p = "a*":
        # ROWS = 2, COLS = 2
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
