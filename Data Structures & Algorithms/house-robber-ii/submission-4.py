class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        def helper(nums):
            prev_max = curr_max = 0
            for num in nums:
                tmp = curr_max
                curr_max = max(curr_max, prev_max + num)
                prev_max = tmp
            return curr_max

        return max(helper(nums[1:]), helper(nums[:-1]))
        