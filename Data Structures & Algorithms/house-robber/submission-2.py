class Solution:
    def rob(self, nums: List[int]) -> int:
        # we only care about best result up to 
        # - previous house
        # - house before that
        prev_max = 0
        curr_max = 0
        for num in nums:
            tmp = curr_max
            curr_max = max(curr_max, prev_max+num)
            prev_max = tmp
        return curr_max
