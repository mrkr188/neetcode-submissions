class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side_len = total // 4
        # sort descending to try larger matchsticks first for faster pruning
        matchsticks.sort(reverse=True)

        # if the longest stick exceeds the target side length, a square is impossible
        if matchsticks[0] > side_len:
            return False
        buckets = [0] * 4

        def backtrack(idx):
            # 1. base case: all matchsticks have been placed
            if idx == len(matchsticks):
                return all(b == side_len for b in buckets)

            for i in range(4):
                # constraint: do not exceed the side length for this bucket
                if buckets[i] + matchsticks[idx] <= side_len:
                    # 3. make choice
                    buckets[i] += matchsticks[idx]

                    # 4. recurse to the next matchstick
                    if backtrack(idx + 1):
                        return True

                    # 5. undo choice (backtracking step)
                    buckets[i] -= matchsticks[idx]

                    # optimization: if this bucket is empty and we failed, 
                    # trying subsequent empty buckets is redundant (symmetry breaking)
                    if buckets[i] == 0:
                        break
    
            return False

        return backtrack(0)