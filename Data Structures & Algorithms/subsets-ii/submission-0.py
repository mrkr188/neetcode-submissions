class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]
        res = [[]]
        dic = collections.Counter(nums)
        for key, val in dic.items():
            tmp = []
            for lst in res:
                for i in range(1, val+1):
                    tmp.append(lst+[key]*i)  
            res += tmp

        return res
        