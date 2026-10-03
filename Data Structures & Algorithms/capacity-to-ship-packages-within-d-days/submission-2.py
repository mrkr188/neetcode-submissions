class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity: int) -> bool:
            curr_weight = 0
            # ship starts with capacity available on day 1, 
            # and a new day begins when the current package cannot fit
            required = 1

            for w in weights:
                # if adding current package exceeds capacity, we need another day
                if curr_weight + w > capacity:
                    required += 1
                    # early exit: if days exceed the limit, this capacity fails
                    if required > days:
                        return False
                    curr_weight = w
                else:
                    curr_weight += w
            return True

        # minimum capacity must be the heaviest single item, 
        # maximum capacity is the sum of all items (shipped in 1 day)
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = m  # save valid capacity
                r = m - 1  # try to find a smaller valid capacity on the left
            else:
                l = m + 1  # capacity too small, need a larger one

        return res



            
        