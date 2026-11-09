class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dists = [(x * x + y * y, x, y) for x, y in points]
        heapq.heapify(dists)

        res = []
        while k > 0:
            k -= 1
            _, x, y = heapq.heappop(dists)
            res.append([x, y])
        return res
