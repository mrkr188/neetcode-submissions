class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # need this when nums is []
        # when nums is [] we get 1 as we are initialize dp[0] = 1
        if not nums:
            return 0

        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]

