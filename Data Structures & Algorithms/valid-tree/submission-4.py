class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        stack = [(0, -1)] # node, prev
        
        while stack:
            node, prev = stack.pop()
            if node in visit:
                return False
            visit.add(node)
            
            for nei in adj[node]:
                # prevents from mistaking edge back to parent node for a cycle, 
                # since every undirected edge connects neighbors both ways.
                if nei == prev:
                    continue
                if nei in visit:
                    return False
                stack.append((nei, node))
                    
        return len(visit) == n

        # def dfs(node, par):
        #     if node in visit:
        #         return False

        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         if not dfs(nei, node):
        #             return False
        #     return True

        # return dfs(0, -1) and len(visit) == n

