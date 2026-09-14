class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(maxCapacity):
            # ship starts with capacity available on day 1, 
            # and a new day begins when the current package cannot fit
            count = 1
            currCapacity = maxCapacity
            for w in weights:
                if currCapacity - w < 0:
                    count += 1
                    if count > days:
                        return False
                    currCapacity = maxCapacity
                
                currCapacity -= w
            return True

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



            
        