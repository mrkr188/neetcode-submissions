class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, temp = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, len(nums)-1
                while l < r:
                    curr = nums[l] + nums[r]
                    if curr < target:
                        l += 1
                    elif curr > target:
                        r -= 1
                    else:
                        res.append(temp + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                return
            
            # to choose k numbers starting from index i, 
            # you need at least k - 1 numbers available after i
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                kSum(k-1, i+1, target - nums[i])
                temp.pop()
            
        kSum(4, 0, target)
        return res



        