class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(candidates)
        candidates.sort()
        
        def dfs(path, target, index):
            if target < 0:
                return
            elif target == 0:
                res.append(path[:])
            else:
                for i in range(index, n):
                    if i>index and candidates[i]==candidates[i-1]:
                        continue
                    dfs(path+[candidates[i]], target-candidates[i], i+1)
        dfs([], target, 0)
        return res