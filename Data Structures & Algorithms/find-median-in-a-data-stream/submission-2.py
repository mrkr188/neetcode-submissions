class MedianFinder:

    def __init__(self):
        self.large = [] # min heap
        self.small = [] # max heap - -ve numbers
        
    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        else:
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))

    def findMedian(self) -> float:
        n1, n2 = len(self.small), len(self.large)
        return -self.small[0] if n1>n2 else (self.large[0] - self.small[0])/2