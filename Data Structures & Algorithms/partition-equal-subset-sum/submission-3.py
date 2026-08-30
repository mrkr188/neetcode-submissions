class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            # we iterate backwards so we don't accidentally reuse the current number 
            # moving left-to-right would let larger sums build on smaller sums we just updated
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
