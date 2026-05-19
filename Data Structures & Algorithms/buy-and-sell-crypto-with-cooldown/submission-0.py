class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)

        return dp[0][1]

        # n = len(prices)
        # dp1_buy, dp1_sell = 0, 0
        # dp2_buy = 0

        # for i in range(n - 1, -1, -1):
        #     dp_buy = max(dp1_sell - prices[i], dp1_buy)
        #     dp_sell = max(dp2_buy + prices[i], dp1_sell)
        #     dp2_buy = dp1_buy
        #     dp1_buy, dp1_sell = dp_buy, dp_sell

        # return dp1_buy
