from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp = []
        # dp.append(nums[0])

        # res = 1
        # for i in range(1, len(nums)):
        #     if dp[-1] < nums[i]:
        #         dp.append(nums[i])
        #         res += 1
        #         continue

        #     idx = bisect_left(dp, nums[i])
        #     dp[idx] = nums[i]

        # return res

        dp = [1] * len(nums)
        maxlen = 1

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    maxlen = max(dp[i], maxlen)
        return maxlen
