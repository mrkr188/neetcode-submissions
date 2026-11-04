class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # ALGORITHM STEPS: WORD BREAK II (TOP-DOWN DP / BACKTRACKING WITH MEMOIZATION)
        #
        # 1. SUBPROBLEMS:  Find all valid space separated sentences for suffix s[start:]
        # 2. STATE:        memo[start] stores list of valid sentences for suffix s[start:]
        # 3. TRANSITION:   For each matching word in wordDict for prefix of s[start:]:
        #                     Combine word with every sentence returned by dfs(start + len(word))
        # 4. ITERATION:    Top-down recursive DFS with memoization to cache suffix solutions
        # 5. BASE:         If start == len(s), return [""] (empty string anchor for sentence joining)
        # 6. RESULT:       dfs(0) returns all valid sentences for full string s[0:]

        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            # return cached result if already computed for this index
            if start in memo:
                return memo[start]

            # base case: reached the end of the string, return empty string indicator
            if start == len(s):
                return [""]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                # constraint: current substring must be a valid dictionary word
                if word in word_set:
                    # recurse to find valid sentences for the remainder of the string
                    sub_sentences = dfs(end)

                    # make choice / build sentence combinations
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            # cache the result for this start index
            memo[start] = res
            return res

        return dfs(0)


