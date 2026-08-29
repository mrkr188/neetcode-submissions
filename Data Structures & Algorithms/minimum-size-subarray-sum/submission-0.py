class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = math.inf
        currSum = 0
        l = 0
        for r, num in enumerate(nums):
            currSum += num
            while currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1

        return 0 if res == math.inf else res


                


        