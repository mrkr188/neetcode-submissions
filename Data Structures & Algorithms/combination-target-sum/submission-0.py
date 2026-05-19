class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()
        n = len(nums)

        def dfs(path, target, index):
            if target == 0:
                res.append(path[:])
            else:
                for i in range(index, n):
                    if target - nums[i] < 0:
                        return
                    # can simplify using
                    dfs(path+[nums[i]], target-nums[i], i)
                    
                    # path.append(nums[i])
                    # dfs(path, target-nums[i], i)
                    # path.pop()
            
        dfs([], target, 0)
        
        return res