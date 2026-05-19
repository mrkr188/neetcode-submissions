class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        curr_max = 0
        for num in nums:
            tmp = curr_max
            curr_max = max(curr_max, prev_max+num)
            prev_max = tmp
        return curr_max