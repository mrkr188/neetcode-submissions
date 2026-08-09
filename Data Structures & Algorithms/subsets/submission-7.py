class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # backtracking template
        # def backtrack(params):
        #     if base_case_condition:
        #         save_result
        #         return

        #     for choice in choices:
        #         if violates_constraints:
        #             continue

        #     make_choice
        #     backtrack(updated_params)
        #     undo_choice  # Backtracking Step

        # res = []
        # subset = []

        # def dfs(i):
        #     if i == len(nums):
        #         res.append(subset.copy())
        #         return
        #     subset.append(nums[i])
        #     dfs(i + 1)
        #     subset.pop()
        #     dfs(i + 1)

        # dfs(0)
        # return res

        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
            # tmp = []
            # for lst in res:
            #     tmp.append(lst+[num])
            # res += tmp
        return res

