class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if '0000' in deadends:
            return -1

        def children(lock):
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                yield lock[:i] + digit + lock[i+1:]
                digit = str((int(lock[i]) - 1 + 10) % 10)
                yield lock[:i] + digit + lock[i+1:]
                 
        visit = set(deadends)
        visit.add('0000')
        queue = deque(['0000'])
        res = 0
        while queue:
            for _ in range(len(queue)):
                lock = queue.popleft()
                if lock == target:
                    return res
                for nei in children(lock):
                    if nei not in visit:
                        visit.add(nei)
                        queue.append(nei)
            res += 1

        return -1