class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(m):
            count = 0
            i = 0
            while i < len(weights):
                diff = m
                while i < len(weights) and weights[i] <= diff:
                    diff -= weights[i]
                    i += 1
                count += 1
            return count <= days

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = (r - l)//2 + l
            if canShip(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res



            
        