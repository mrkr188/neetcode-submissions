class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-v for k,v in count.items()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque() # [-count, time when the task can processed]

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    queue.append([cnt, time + n])
            else:
                # for example if tasks = [AAAAAA] and n = 3
                # we'd be looping n*len(tasks) times without this else
                # here we just update time directly and reduce number of inerations
                time = queue[0][1]
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time


