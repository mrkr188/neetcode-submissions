class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        n = len(nums)
        res = []
        def helper(res, l):
            if l == n-1:
                res.append(nums[:])
            else:
                for i in range(l, n):
                    nums[i], nums[l] = nums[l], nums[i]
                    helper(res, l+1)
                    nums[i], nums[l] = nums[l], nums[i]
        helper(res, 0)
        return res

        # # iterative
        # perms = [[]]
        # for num in nums:
        #     new_perms = []
        #     for p in perms:
        #         for i in range(len(p) + 1):
        #             p_copy = p.copy()
        #             p_copy.insert(i, num)
        #             new_perms.append(p_copy)
        #     perms = new_perms
        # return perms