class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            curMax, curMin=max(num, num*curMax, num*curMin), min(num, num*curMax, num*curMin)
            res = max(res, curMax)
        return res