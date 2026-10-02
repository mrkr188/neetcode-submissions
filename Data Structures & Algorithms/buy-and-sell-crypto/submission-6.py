class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        l = 0
        maxProfit = 0
        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            # this means we found cheaper buy price
            else:
                l = r
        return maxProfit

