class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        # prefix_sum -> count of occurrences
        # {0: 1} base case handles subarrays starting directly at index 0
        prefixSums = {0: 1}

        for num in nums:
            # accumulate running sum from index 0 to current position
            curSum += num

            # required previous prefix sum: curSum - prevPrefix = k
            diff = curSum - k

            # add occurrences of valid starting prefix sums
            res += prefixSums.get(diff, 0)

            # record frequency of current running prefix sum
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res