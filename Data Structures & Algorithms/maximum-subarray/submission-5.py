class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        curr = 0
        for num in nums:
            curr = max(curr+num, num)
            res = max(curr, res)
        return res