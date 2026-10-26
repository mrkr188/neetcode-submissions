class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # 1. Build the Trie from the dictionary
        root = TrieNode()
        for word in dictionary:
            curr = root
            for c in word:
                curr = curr.children[c]
            curr.is_word = True

        n = len(s)
        dp = [0] * (n + 1)

        # 2. Bottom-up DP from right to left
        for i in range(n - 1, -1, -1):
            # Choice 1: Treat s[i] as an extra character (cost = 1 + remaining)
            dp[i] = 1 + dp[i + 1]

            # Choice 2: Walk the Trie to find any matching dictionary words starting at i
            curr = root
            for j in range(i, n):
                # if s[j] not in curr.children:
                #     break  
                curr = curr.children[s[j]]
                if not curr: # No dictionary word starts with this prefix
                    break
                if curr.is_word:
                    # We found a valid dictionary word ending at index j!
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]

        # n = len(s)
        # # dp[i] represents the minimum extra characters needed
        # # for the substring starting from index i to the end (s[i:])
        # dp = [0] * (n + 1)

        # # Iterate backwards from right to left (bottom-up DP)
        # for i in range(n - 1, -1, -1):
        #     # Choice 1: Treat the current character s[i] as "extra" (cost = 1 + remaining)
        #     dp[i] = 1 + dp[i + 1]

        #     # Choice 2: Check if any dictionary word can match starting at index i
        #     for word in dictionary:
        #         if i + len(word) <= n and s[i : i + len(word)] == word:
        #             # If it matches, we add 0 extra cost for this word
        #             # and take the dp value right after the word ends
        #             dp[i] = min(dp[i], dp[i + len(word)])

        # # dp[0] gives the minimum extra characters for the entire string
        # return dp[0]