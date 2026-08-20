class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0]*numCourses
        adj = defaultdict(list)
        for dst, src in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        finished = 0
        queue = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)
                finished += 1

        while queue:
            c = queue.popleft()
            for preq in adj[c]:
                indegree[preq] -= 1
                if indegree[preq] == 0:
                    queue.append(preq)
                    finished += 1
        return finished == numCourses

        # preqMap = defaultdict(list)
        # for c, p in prerequisites:
        #     preqMap[p].append(c)
        
        # visited = set()

        # def dfs(course):
        #     if course in visited:
        #         return False
        #     if preqMap[course] == []:
        #         return True
        #     visited.add(course)
        #     for preq in preqMap[course]:
        #         if not dfs(preq):
        #             return False
        #     preqMap[course] = []
        #     visited.remove(course)
        #     return True
        
        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True



        