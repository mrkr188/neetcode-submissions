class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # ALGORITHM STEPS: WORD BREAK II (TOP-DOWN DP / BACKTRACKING WITH MEMOIZATION)
        #
        # 1. SUBPROBLEMS:  Find all valid space-separated sentences for suffix s[start:]
        # 2. STATE:        memo[start] stores list of valid sentences for suffix s[start:]
        # 3. TRANSITION:   For each matching word in wordDict for prefix of s[start:]:
        #                     Combine word with every sentence returned by dfs(start + len(word))
        # 4. ITERATION:    Top-down recursive DFS with memoization to cache suffix solutions
        # 5. BASE:         If start == len(s), return [""] (empty string anchor for sentence joining)
        # 6. RESULT:       dfs(0) returns all valid sentences for full string s[0:]

        word_set = set(wordDict)
        memo = {}

        def dfs(start: int) -> List[str]:
            if start in memo:
                return memo[start]

            # base case: reached end of string
            if start == len(s):
                return [""]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # recurses on remaining suffix
                    sub_sentences = dfs(end)
                    for sub in sub_sentences:
                        sentence = f"{word} {sub}".strip()
                        res.append(sentence)

            memo[start] = res
            return res

        return dfs(0)

        # evaluated execution trace for s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]:
        # len(s) = 10
        #
        # dfs(10) -> [""]
        # dfs(7)  ["dog"]:
        #           matches "dog" -> "dog" + dfs(10) -> ["dog"]
        # dfs(4)  ["sanddog"]:
        #           matches "sand" -> "sand" + dfs(7) -> ["sand dog"]
        # dfs(3)  ["sanddog"]:
        #           matches "and" -> "and" + dfs(7) -> ["and dog"]
        # dfs(0)  ["catsanddog"]:
        #           matches "cat"  -> "cat"  + dfs(3) -> ["cat and dog"]
        #           matches "cats" -> "cats" + dfs(4) -> ["cats sand dog"]
        #
        # final output: ["cat and dog", "cats sand dog"]