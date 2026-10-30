class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        
        def backtrack(path, index, target):
            if target == 0:
                res.append(path[:])
            else:
                for i in range(index, n):
                    if i > index and nums[i] == nums[i-1]:
                        continue
                    if target - nums[i] < 0:
                        break
                    backtrack(path + [nums[i]], i + 1, target - nums[i])
        
        backtrack([], 0, target)
        return res
