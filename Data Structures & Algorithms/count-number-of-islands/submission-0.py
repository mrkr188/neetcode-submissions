class Solution:

    # def dfs(grid,i,j):
    #     if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
    #         return 
    #     if grid[i][j]=='1': 
    #         grid[i][j]='0'
    #         dfs(grid,i+1,j)
    #         dfs(grid,i-1,j)
    #         dfs(grid,i,j+1)
    #         dfs(grid,i,j-1)
    # count = 0 
    # for i in range(len(grid)): 
    #     for j in range(len(grid[0])): 
    #         if grid[i][j]=='1': 
    #             count +=1
    #             dfs(grid,i,j)
    # return count
    
    def bfs(self, grid, start):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        n, m = len(grid), len(grid[0])
        queue = collections.deque()
        queue.append(start)
        grid[start[0]][start[1]] = '0'
        while len(queue):
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []: return 0
        ans, n, m = 0, len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    self.bfs(grid, (i, j))
                    
        return ans