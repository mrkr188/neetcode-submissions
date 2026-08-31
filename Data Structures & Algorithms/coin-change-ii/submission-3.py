class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # dp[a] stores the number of ways to make target amount a
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            # left-to-right iteration allows using the current coin multiple times
            # unlike - https://neetcode.io/problems/partition-equal-subset-sum/question
            for a in range(1, amount+1):
                # add combinations formed by including the current coin
                dp[a] += dp[a - coin] if coin <= a else 0
        return dp[amount]

# dp matrix state progression for coins = [1, 2], amount = 3:
#
#                 a = 0     a = 1     a = 2     a = 3
#               +---------+---------+---------+---------+
# init          |    1    |    0    |    0    |    0    |  base case: 1 way to make 0
#               +---------+---------+---------+---------+
# after coin 1  |    1    |    1    |    1    |    1    |  dp[a] += dp[a - 1]
#               +---------+---------+---------+---------+
# after coin 2  |    1    |    1    |    2    |    2    |  dp[a] += dp[a - 2]
#               +---------+---------+---------+---------+
#
# dp[a] means: number of ways to form amount 'a' using coins processed so far
