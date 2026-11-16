class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # append original index to each task and sort by enqueue time 
        # (stable sort preserves tie-breaks)
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key = lambda t: t[0])

        min_heap = []
        res = []
        time = i = 0
        n = len(tasks)

        while min_heap or i < n:
            # push all available tasks into the min-heap: (processing_time, original_index)
            while i < n and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if not min_heap:
                # fast-forward time to the next available task
                time = tasks[i][0]
            else:
                # execute the task with the shortest processing time
                proc_time, idx = heapq.heappop(min_heap)
                time += proc_time
                res.append(idx)

        return res