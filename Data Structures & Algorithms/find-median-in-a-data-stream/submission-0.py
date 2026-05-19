from heapq import heappush, heappushpop

class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:        
        if len(self.small) == len(self.large):
            heappush(self.small, -heappushpop(self.large, -num))
        else:
            heappush(self.large, -heappushpop(self.small, num))

    def findMedian(self) -> float:
        n1, n2 = len(self.small), len(self.large)
        return self.small[0] if n1>n2 else (self.small[0]-self.large[0])/2


