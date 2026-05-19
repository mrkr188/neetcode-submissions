class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        return max(self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        curr_max = 0
        prev_max = 0
        for num in nums:
            tmp = curr_max
            curr_max = max(curr_max, prev_max+num)
            prev_max = tmp
        return curr_max