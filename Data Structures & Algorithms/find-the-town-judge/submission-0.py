class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0]*(n+1)
        adj = defaultdict(list)
        for u, v in trust:
            adj[u].append(v)
            indegree[v] += 1
        
        for i in range(1, n+1):
            if indegree[i] == n-1 and adj[i] == []:
                return i
        return -1

        