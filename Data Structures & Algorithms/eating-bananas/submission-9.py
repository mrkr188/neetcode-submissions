class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l+r)//2
            totalTime = sum([math.ceil(pile/m) for pile in piles])
            if totalTime <= h:
                res = m
                r = m-1
            else:
                l = m+1
        return res




