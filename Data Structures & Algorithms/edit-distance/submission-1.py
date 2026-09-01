class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        rows, cols = len(word1), len(word2)
        # dp uses 1-based string lengths to fit the empty string base cases at index 0
        # since row 0 is for the empty string, length r maps to index r - 1 in the string
        # approach: bottom-up dp tracking minimum operations to convert word1[:r] to word2[:c]
        # dp[r][c] = min edit distance between prefixes word1[:r] and word2[:c]
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows + 1):
            for c in range(cols + 1):
                # base case: empty word1 requires c insertions to make word2[:c]
                if r == 0:
                    dp[r][c] = c

                # base case: empty word2 requires r deletions from word1[:r]
                elif c == 0:
                    dp[r][c] = r

                # characters match: no new op needed, take diagonal
                elif word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]

                # characters differ: 1 + min(insert, delete, replace)
                else:
                    dp[r][c] = 1 + min(
                        dp[r][c - 1],    # insert
                        dp[r - 1][c],    # delete
                        dp[r - 1][c - 1] # replace
                    )

        # min edit distance to convert full word1 to full word2
        return dp[rows][cols]


        # ALGORITHM STEPS: EDIT DISTANCE (BOTTOM-UP DP)
        #
        # 1. SUBPROBLEMS: Find minimum operations to convert suffix word1[i:] to word2[j:]
        # 2. STATE:       dp[i][j] is min operations to convert word1[i:] to word2[j:]
        # 3. TRANSITION:  If characters match:
        #                     No operation needed, advance both pointers
        #                 If characters differ:
        #                     Take 1 + minimum of Insert (advance word2),
        #                     Delete (advance word1), or Replace (advance both)
        # 4. ITERATION:   Loop i backwards (len1 down to 0), j backwards (len2 down to 0)
        # 5. BASE:        Matching any suffix with an empty string costs remaining length
        # 6. RESULT:      dp[0][0] represents min operations to convert word1 into word2
        #
        # evaluated grid for word1 = "horse", word2 = "ros":
        #
        #                    c = 0        c = 1        c = 2        c = 3
        #                   (empty)       ('r')        ('o')        ('s')
        #                 +------------+------------+------------+------------+
        #  r = 0 (empty)  |     0      |     1      |     2      |     3      |
        #                 +------------+------------+------------+------------+
        #  r = 1 ('h')    |     1      |     1      |     2      |     3      |
        #                 +------------+------------+------------+------------+
        #  r = 2 ('o')    |     2      |     2      |     1      |     2      |
        #                 +------------+------------+------------+------------+
        #  r = 3 ('r')    |     3      |     2      |     2      |     2      |
        #                 +------------+------------+------------+------------+
        #  r = 4 ('s')    |     4      |     3      |     3      |     2      |
        #                 +------------+------------+------------+------------+
        #  r = 5 ('e')    |     5      |     4      |     4      |     3      |
        #                 +------------+------------+------------+------------+