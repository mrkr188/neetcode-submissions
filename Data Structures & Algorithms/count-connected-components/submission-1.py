class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        res = 0
        for node in range(n):
            if node not in visit:
                res += 1
                visit.add(node)
                stack = [node]
                while stack:
                    curr = stack.pop()
                    for nei in adj[curr]:
                        if nei not in visit:
                            visit.add(nei)
                            stack.append(nei)
        return res
                        

        # def dfs(node):
        #     for nei in adj[node]:
        #         if nei not in visit:
        #             visit.add(nei)
        #             dfs(nei)

        # res = 0
        # for node in range(n):
        #     if node not in visit:
        #         visit.add(node)
        #         dfs(node)
        #         res += 1
        # return res

