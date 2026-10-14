class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def canSplit(largest):
            subarrays = 0
            i = 0
            while i < n:
                l, r = i + 1, n
                while l <= r:
                    mid = l + (r - l) // 2
                    if prefix[mid] - prefix[i] <= largest:
                        l = mid + 1
                    else:
                        r = mid - 1
                subarrays += 1
                i = r
                if subarrays > k:
                    return False
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

        
