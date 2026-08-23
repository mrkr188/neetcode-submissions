class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        N = len(points)
        for p in range(N):
            x1, y1 = points[p]
            for q in range(p+1, N):
                x2, y2 = points[q]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[p].append((dist, q))
                adj[q].append((dist, p))
        
        minHeap = [(0, 0)] # (cost, node)
        visited = set()
        res = 0
        while len(visited) < N:
            dist1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            visited.add(node1)
            res += dist1
            for dist2, node2 in adj[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (dist2, node2))
        return res


