class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        n = len(nums)

        def dfs(index):
            if index == n-1:
                res.append(nums[:])
            else:
                for i in range(index, n):
                    nums[i], nums[index] = nums[index], nums[i]
                    dfs(index+1)
                    nums[i], nums[index] = nums[index], nums[i]
        dfs(0)
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