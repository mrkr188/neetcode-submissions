class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -math.inf
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum+num, num)
            res = max(curr_sum, res)
        return res