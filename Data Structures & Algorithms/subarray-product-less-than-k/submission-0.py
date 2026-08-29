class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        l = 0
        currProduct = 1
        res = 0

        for r in range(len(nums)):
            currProduct *= nums[r]
            while l <= r and currProduct >= k:
                currProduct //= nums[l]
                l += 1
            res += (r - l + 1)

        return res




        