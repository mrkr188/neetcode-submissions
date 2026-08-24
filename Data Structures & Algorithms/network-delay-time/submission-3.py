class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        res = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            # why we need this check?
            # checking before pushing only prevents duplicates at that exact moment, 
            # but multiple valid paths can still sneak into the heap before a node is 
            # officially popped and marked visited
            if n1 in visit:
                continue
            visit.add(n1)
            res = w1

            # end early if we visited all nodes
            if len(visit) == n:
                return res

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return res if len(visit) == n else -1


        