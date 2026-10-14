class Solution:

    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # build prefix sum array for fast range-sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # helper function to check if we can split nums into <= k subarrays with max sum <= largest
        def canSplit(largest):
            subarrays = 0
            i = 0
            end = n
            while i < n:
                # binary search to find the farthest valid end index for the current subarray
                l, r = i + 1, n
                while l <= r:
                    mid = l + (r - l) // 2
                    if prefix[mid] - prefix[i] <= largest:
                        end = mid
                        l = mid + 1
                    else:
                        r = mid - 1
                subarrays += 1
                i = end  # jump to the end of the valid subarray
                if subarrays > k:
                    return False
            return True

        # binary search range for the minimum possible largest subarray sum
        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = (r - l) // 2 + l

            if canSplit(m):
                res = m
                r = m - 1  # try to find a smaller valid maximum sum
            else:
                l = m + 1  # fix: was l = l + 1; since m is too small, shift lower bound past m

        return res

        
