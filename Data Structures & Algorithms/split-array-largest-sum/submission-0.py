class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            currSum = 0
            splits = 1
            for num in nums:
                currSum += num
                if currSum > largest:
                    splits += 1
                    if splits > k:
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

        
