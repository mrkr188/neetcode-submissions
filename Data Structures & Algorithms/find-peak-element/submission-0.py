class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums)
        res = 0
        
        while l <= r:
            m = l + (r - l)//2
            if m == len(nums) - 1 or nums[m] > nums[m+1]:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
        