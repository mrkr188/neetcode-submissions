class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r]-prices[l])
            # this just means we found cheaper buy price
            else:
                l = r
            r += 1

        return maxProfit
