class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        for s, d, cost in flights:  # s=source, d=dest, p=cost
            adj[s].append([d, cost])

        q = deque([(0, src, 0)])
        while q:
            currCost, node, stops = q.popleft()
            if stops > k:
                continue

            for nei, w in adj[node]:
                nextCost = currCost + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1

