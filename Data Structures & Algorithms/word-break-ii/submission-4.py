class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # ALGORITHM STEPS: WORD BREAK II WITH TRIE OPTIMIZATION
        #
        # 1. BUILD TRIE:    Insert all words from wordDict into a prefix tree
        # 2. SUBPROBLEMS:   Find all valid space-separated sentences for suffix s[start:]
        # 3. STATE:         cache[start] stores list of valid sentences for suffix s[start:]
        # 4. TRANSITION:    Walk the trie from start; if a valid word node is reached,
        #                   combine it with every sentence returned by dfs(end)
        # 5. EARLY EXIT:    Break out of the loop early if the character path doesn't exist in the trie
        # 6. BASE:          If start == len(s), return [""] (empty string anchor for sentence joining)

        # 1. build the trie
        trie = TrieNode()
        for word in wordDict:
            curr = trie
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_word = True

        cache = {}

        def dfs(start):
            if start in cache:
                return cache[start]

            if start == len(s):
                return [""]

            res = []
            curr = trie
            # walk the string and the trie simultaneously
            for end in range(start, len(s)):
                char = s[end]
                # early exit: if path doesn't exist in trie, no further prefixes are valid
                if char not in curr.children:
                    break
                curr = curr.children[char]

                # if we hit a valid dictionary word ending, recurse for the remainder
                if curr.is_word:
                    word = s[start : end + 1]
                    sub_sentences = dfs(end + 1)

                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            cache[start] = res
            return res

        return dfs(0)

