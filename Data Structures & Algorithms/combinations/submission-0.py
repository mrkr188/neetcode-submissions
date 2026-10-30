class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(path, start):
            if len(path) == k:
                res.append(path[:])
            else:
                for num in range(start, n + 1):
                    backtrack(path + [num], num + 1)
        
        backtrack([], 1)
        return res