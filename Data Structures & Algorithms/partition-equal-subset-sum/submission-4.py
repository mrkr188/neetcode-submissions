class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        # odd total sum can never be split into two equal integer subsets
        if total % 2:
            return False

        target = total // 2

        # dp[j] stores whether a subset sum equal to j is possible
        dp = [False] * (target + 1)

        # base case: sum 0 is always possible with an empty subset
        dp[0] = True

        for num in nums:
            # iterate backwards so we don't accidentally reuse the current number 
            # moving left-to-right would let larger sums build on smaller sums we just updated             
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        # return whether target sum is achievable
        return dp[target]


#       dp state progression for nums = [1, 2, 3], target = 3:
#
#                 j = 0     j = 1     j = 2     j = 3
#               +---------+---------+---------+---------+
# init          |  True   |  False  |  False  |  False  |  base case: sum 0 is always possible
#               +---------+---------+---------+---------+
# after num 1   |  True   |  True   |  False  |  False  |  dp[j] = dp[j] or dp[j - 1]
#               +---------+---------+---------+---------+
# after num 2   |  True   |  True   |  True   |  True   |  dp[j] = dp[j] or dp[j - 2]
#               +---------+---------+---------+---------+
# after num 3   |  True   |  True   |  True   |  True   |  dp[j] = dp[j] or dp[j - 3]
#               +---------+---------+---------+---------+
#
#       dp[j] means: can a subset sum to 'j' using numbers processed so far