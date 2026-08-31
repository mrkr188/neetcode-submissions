class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        # i is index of s, j is index of t
        # (i, j) -> count of distinct subsequences
        dp = {} 

        # top-down dfs with memoization counts ways to match t[j:] within s[i:]
        # when chars match, we sum choices to match or skip s[i]; if not, we must skip s[i]
        def dfs(i, j):

            # if we reach end of t, we have count 1
            if j == len(t):
                return 1
            # when we reach end of s, count is 0 since we didn't find any match
            if i == len(s):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)
            
            return dp[(i, j)]
        
        return dfs(0, 0)
        