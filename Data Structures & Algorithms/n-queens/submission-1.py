class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        colSet = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [['.']*n for _ in range(n)]

        def dfs(r):
            if r == n:
                res.append([''.join(board[row]) for row in range(n)])
            else:
                for c in range(n):
                    if c in colSet or r+c in posDiag or r-c in negDiag:
                        continue

                    board[r][c] = 'Q'
                    colSet.add(c)
                    posDiag.add(r+c)
                    negDiag.add(r-c)
                    dfs(r+1)

                    board[r][c] = '.'
                    colSet.remove(c)
                    posDiag.remove(r+c)
                    negDiag.remove(r-c)
        dfs(0)
        return res



