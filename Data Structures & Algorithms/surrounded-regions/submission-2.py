class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return
        
        m = len(board)
        n = len(board[0])
        
        edges = [(i, j) for i in [0, m-1] for j in range(n)] + \
                [(i, j) for i in range(1,m-1) for j in [0, n-1]]
        
        for row, col in edges:
            if board[row][col] == 'O':
                board[row][col] = 'S'
                stack = [(row, col)]
                while stack:
                    r, c = stack.pop()
                    for i, j in [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]:
                        if 0 < i < m and 0 < j < n and board[i][j] == 'O':
                            board[i][j] = 'S'
                            stack.append((i, j))
                            
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'S':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
        

        # ROWS, COLS = len(board), len(board[0])
        # zeros = set()
        
        # def dfs(r, c):
        #     if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or board[r][c] == 'X' or (r,c) in zeros:
        #         return
        #     zeros.add((r, c))
        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)

        # for r in range(ROWS):
        #     dfs(r, 0)
        #     dfs(r, COLS - 1)

        # for c in range(COLS):
        #     dfs(0, c)
        #     dfs(ROWS - 1, c)
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r, c) not in zeros:
        #             board[r][c] = 'X'
