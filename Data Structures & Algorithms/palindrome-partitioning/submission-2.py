class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        # Precompute palindrome table to avoid repeated checks and slicing
        # dp[i][j] will be True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        res = []
        
        def dfs(start, path):
            if start == n:
                res.append(list(path))
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


