class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        ROWS, COLS = len(heights), len(heights[0])
        def neibhours(node):
            x, y = node
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                r, c = x+dx, y+dy
                if 0 <= r < ROWS and 0 <= c < COLS:
                    yield r, c
        

        minHeap = [[0, 0, 0]] # max effort so far, row, col
        visit = set()

        while minHeap:
            curr_max, r, c = heapq.heappop(minHeap)

            if (r, c) in visit:
                continue
            visit.add((r, c))

            if (r, c) == (ROWS-1, COLS-1):
                return curr_max

            for nr, nc in neibhours((r, c)):
                new_max = max(abs(heights[nr][nc] - heights[r][c]), curr_max)
                heapq.heappush(minHeap, (new_max, nr, nc))


