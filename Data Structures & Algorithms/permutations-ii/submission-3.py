class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        def permutation(remaining, path):
            if len(remaining) == 0:
                res.append(path)

            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i-1]:
                    continue
                permutation(remaining[0:i]+remaining[i+1:], path + [remaining[i]])
        
        nums.sort()

        permutation(nums, [])
        return res


