class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        indegree = [0]*numCourses
        adj = defaultdict(set)
        preqMap = defaultdict(set)
        for s, d in prerequisites:
            adj[s].add(d)
            indegree[d] += 1
        
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])
        while queue:
            node = queue.popleft()
            for nei in adj[node]:
                # nei has node as preq
                preqMap[nei].add(node)
                # all preq of node are also preq for nei
                preqMap[nei].update(preqMap[node])
                indegree[nei] -= 1
                # when nei does't have any more preqs (indegree=0) add it to queue
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return [u in preqMap[v] for u, v in queries]




        
        


        
        