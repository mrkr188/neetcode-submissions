class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        m = len(board)
        n = len(board[0])
        
        w = len(word)
        
        def dfs(board, start, ix):
            
            if ix == w:
                return True
            
            i,j = start
            
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[ix]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'  # to prevent looping
            
            for x,y in zip(dx,dy):
                x += i
                y += j
                if dfs(board, (x,y), ix+1):
                    return True
            
            board[i][j] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(board, (i,j), 0):
                    return True
                    
        return False