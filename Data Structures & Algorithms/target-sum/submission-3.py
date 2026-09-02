class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # need this when nums is []
        # when nums is [] we get 1 as we initialize dp[0] = 1
        if not nums:
            return 0

        # ALGORITHM STEPS: TARGET SUM (BOTTOM-UP SUBSET SUM DP)
        #
        # 1. SUBPROBLEMS: Count ways to pick subset from nums[i:] summing to target t
        # 2. STATE:       dp[i][t] is total subset combinations from nums[i:] for sum t
        # 3. TRANSITION:  For current element nums[i]:
        #                     Sum of including nums[i] (advance i, reduce target)
        #                     plus skipping nums[i] (advance i, keep target)
        # 4. ITERATION:   Loop i backwards (n down to 0), target t from 0 up to S
        # 5. BASE:        dp[n][0] = 1 (1 way to form target sum 0 using empty suffix)
        # 6. RESULT:      dp[0][S] is ways to form target sum S using all elements
        
        dp = defaultdict(int) # total, count
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]

