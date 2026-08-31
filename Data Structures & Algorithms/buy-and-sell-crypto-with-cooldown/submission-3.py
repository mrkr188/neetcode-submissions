class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp1_buy = 0 # profit if we can buy next day
        dp1_sell = 0 # profit if we can sell next day
        dp2_buy = 0 # profit if we can buy two day after (sell now and cooldown next day)

        for i in range(len(prices)-1, -1, -1):
            # profit if we can buy/cooldown today choose max of 
            #   - buy now and sell next day
            #   - cooldown now and buy next day
            buy = max(dp1_sell - prices[i], dp1_buy)
            # profit if we can sell/cooldown today choose max of 
            #   - sell now and cooldown next day
            #   - cooldown now and sell next day
            sell = max(dp2_buy + prices[i], dp1_sell)
            
            dp2_buy = dp1_buy
            dp1_buy, dp1_sell = buy, sell
        
        return dp1_buy

        # n = len(prices)
        # dp = [[0] * 2 for _ in range(n + 1)]

        # for i in range(n - 1, -1, -1):
        #     for buying in [True, False]:
        #         if buying:
        #             buy = dp[i + 1][False] - prices[i] if i + 1 < n else -prices[i]
        #             cooldown = dp[i + 1][True] if i + 1 < n else 0
        #             dp[i][1] = max(buy, cooldown)
        #         else:
        #             sell = dp[i + 2][True] + prices[i] if i + 2 < n else prices[i]
        #             cooldown = dp[i + 1][False] if i + 1 < n else 0
        #             dp[i][0] = max(sell, cooldown)

        # return dp[0][1]
