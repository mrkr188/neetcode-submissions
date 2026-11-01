class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # precompute palindrome table to avoid repeated checks and slicing
        # dp[r][c] will be True if s[r:c+1] is a palindrome
        # evaluate the 2d table using a bottom-up triangular traversal:
        # ["O", "O", "O", "O", "O"],  # r = 0
        # ["X", "O", "O", "O", "O"],  # r = 1
        # ["X", "X", "O", "O", "O"],  # r = 2
        # ["X", "X", "X", "O", "O"],  # r = 3
        # ["X", "X", "X", "X", "O"]   # r = 4
        # (processed bottom-to-top, row by row, from left to right)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for r in range(n - 1, -1, -1):
            for c in range(r, n):
                if s[r] == s[c] and (c - r <= 2 or dp[r + 1][c - 1]):
                    dp[r][c] = True

        res = []
        
        def dfs(start, path):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end + 1])
                    dfs(end + 1, path)
                    path.pop()

        dfs(0, [])
        return res

        # def dfs(s, path, res):
        #     if not s:
        #         res.append(path[:])
        #         return
        #     for i in range(1, len(s)+1):
        #         if s[:i] == s[i-1::-1]:
        #             path.append(s[:i])
        #             dfs(s[i:], path, res)
        #             path.pop()
                    
        # res = []
        # dfs(s, [], res)
        # return res


