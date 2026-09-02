class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # ALGORITHM STEPS: WORD BREAK (BOTTOM-UP DP)
        #
        # 1. SUBPROBLEMS: Check if suffix s[i:] can be segmented into dictionary words
        # 2. STATE:       dp[i] is True if suffix s[i:] can be partitioned into valid words
        # 3. TRANSITION:  For current index i, check each word in dictionary:
        #                     If word matches prefix starting at s[i] and remainder
        #                     suffix starting after word is valid, then dp[i] is True
        # 4. ITERATION:   Loop index i backwards (length down to 0)
        # 5. BASE:        dp[length] = True (empty suffix is always valid)
        # 6. RESULT:      dp[0] shows if the full string s[0:] can be segmented  
         
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

