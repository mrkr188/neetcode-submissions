class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            n, d = eq
            adj[n].append([d, values[i]])
            adj[d].append([n, 1 / values[i]])
        
        def bfs(src, target):

            if src not in adj or target not in adj:
                return -1
            
            seen = set([src])
            queue = deque([[src, 1]])

            while queue:
                curr, curr_weight = queue.popleft()
                if curr == target:
                    return curr_weight

                for nei, weight in adj[curr]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append([nei, curr_weight * weight])
            return -1
        
        return [bfs(src, dst) for src, dst in queries]
        



        