class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(path, left, right):
            if left == right == n:
                res.append(path[:])
            else:
                if left < n:
                    dfs(path+['('], left+1, right)
                if right < left:
                    dfs(path+[')'], left, right+1)
        dfs([], 0, 0)
        return [''.join(lst) for lst in res]


