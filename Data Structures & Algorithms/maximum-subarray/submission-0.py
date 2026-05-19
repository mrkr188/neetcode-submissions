class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -math.inf
        list = []
        for i in nums:
            curr_sum = max(i, curr_sum+i)
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum