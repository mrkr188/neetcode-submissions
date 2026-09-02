class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # ALGORITHM STEPS: COIN CHANGE II (BOTTOM-UP UNBOUNDED KNAPSACK DP)
        #
        # 1. SUBPROBLEMS: Count ways to make amount a using coin types from coins[i:]
        # 2. STATE:       dp[i][a] is total combinations forming amount a using coins[i:]
        # 3. TRANSITION:  For current coin type coins[i]:
        #                     Sum of using coins[i] (keep index i, reduce amount)
        #                     plus skipping coins[i] (advance to index i+1)
        # 4. ITERATION:   Loop i backwards (n down to 0), amount a from 0 up to target
        # 5. BASE:        dp[i][0] = 1 (1 way to make amount 0: use no coins)
        # 6. RESULT:      dp[0][amount] is total ways to make full amount using all coins
        
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
