class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            currSum = 0
            # start at 1: build 1st subarray until overflow starts the next
            subarray = 1
            for num in nums:
                currSum += num
                if currSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    currSum = num
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (r - l)//2 + l
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = l + 1
        return res

        
