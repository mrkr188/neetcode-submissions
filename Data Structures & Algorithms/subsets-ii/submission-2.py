class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]
        res = [[]]
        d = Counter(nums)
        for key, val in d.items():
            tmp = []
            for lst in res:
                for i in range(1, val+1):
                    tmp.append(lst+[key]*i)  
            res += tmp

        return res
        