class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]

        adj = defaultdict(list)
        indegree = [0]*n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        queue = deque([node for node in range(n) if indegree[node] == 1])

        while queue:
            if n <= 2:
                return list(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                n -= 1
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        queue.append(nei)

        

        