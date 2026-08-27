class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        N = len(grid)
        def neibhours(node):
            x,y = node
            res = []
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                r, c = x+dx, y+dy
                if 0 <= r < N and 0 <= c < N:
                    res.append((r, c))
            return res
        
        minHeap = [(grid[0][0], (0,0))] # (time/max-height, (r, c))
        seen = set()

        while minHeap:
            time1, node1 = heapq.heappop(minHeap)

            if node1 in seen:
                continue
            if node1 == (N-1, N-1):
                return time1
            seen.add(node1)

            for node2 in neibhours(node1):
                if node2 not in seen:
                    time2 = grid[node2[0]][node2[1]]
                    heapq.heappush(minHeap, (max(time1, time2), node2))



