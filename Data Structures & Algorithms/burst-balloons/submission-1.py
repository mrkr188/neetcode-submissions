class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # approach: bottom-up interval dp operating on balloon ranges [l, r].
        # dp[l][r] = max coins gained by bursting all balloons from index l to r.
        #
        # to calculate dp[l][r], pick balloon i as the LAST popped in range [l, r]:
        # 1. outer neighbors remain fixed at l - 1 and r + 1 -> new_nums[l-1] * new_nums[i] * new_nums[r+1]
        # 2. balloon i splits range into independent subproblems -> dp[l][i-1] + dp[i+1][r]
        # 3. dp[l][r] = max over all choices of i from l to r
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

