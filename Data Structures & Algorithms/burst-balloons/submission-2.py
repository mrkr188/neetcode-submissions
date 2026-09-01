class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # ALGORITHM STEPS: BURST BALLOONS (BOTTOM-UP INTERVAL DP)
        #
        # 1. SUBPROBLEMS: Find maximum coins gained from bursting all balloons in [l, r]
        # 2. STATE:       dp[l][r] is max coins obtainable from interval [l, r]
        # 3. TRANSITION:  Pick balloon i as the last to burst in interval [l, r]:
        #                     Coins = product of boundary neighbors and balloon i
        #                             + max coins from left subinterval [l, i-1]
        #                             + max coins from right subinterval [i+1, r]
        #                     Take the maximum coins over all valid choices of balloon i
        # 4. ITERATION:   Outer loop l backwards (n down to 1), inner loop r from l to n
        # 5. BASE:        Empty intervals (l > r) yield 0 coins
        # 6. RESULT:      dp[1][n] is the maximum coins for the full range [1, n]
        #
        # evaluated grid including padded boundaries (0 and n+1) for nums = [3, 1, 5]:
        # new_nums = [1, 3, 1, 5, 1]
        #
        #                r=0(val:1)   r=1(val:3)   r=2(val:1)   r=3(val:5)   r=4(val:1)
        #               +------------+------------+------------+------------+------------+
        #  l=0 (val:1)  |     0      |     0      |     0      |     0      |     0      |
        #               +------------+------------+------------+------------+------------+
        #  l=1 (val:3)  |     0      |     3      |     15     |    167     |     0      |
        #               +------------+------------+------------+------------+------------+
        #  l=2 (val:1)  |     0      |     0      |     1      |     40     |     0      |
        #               +------------+------------+------------+------------+------------+
        #  l=3 (val:5)  |     0      |     0      |     0      |     15     |     0      |
        #               +------------+------------+------------+------------+------------+
        #  l=4 (val:1)  |     0      |     0      |     0      |     0      |     0      |
        #               +------------+------------+------------+------------+------------+

        n = len(nums)
        # pad array with boundary 1s to simplify border checks
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # l iterates backward from n to 1 to build smaller sub-intervals first
        for l in range(n, 0, -1):
            # r expands forward from l to n
            for r in range(l, n + 1):
                # i represents the LAST balloon popped in range [l, r]
                for i in range(l, r + 1):
                    # coins gained when balloon i is popped last in [l, r]
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    # add max coins from remaining left [l, i-1] and right [i+1, r] sub-ranges
                    coins += dp[l][i - 1] + dp[i + 1][r]

                    dp[l][r] = max(dp[l][r], coins)

        # return max coins for full range [1, n]
        return dp[1][n]

