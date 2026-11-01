class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        def permutation(numbers, path):
            if len(numbers) == 0:
                res.append(path)

            for i in range(len(numbers)):
                if i > 0 and numbers[i] == numbers[i-1]:
                    continue
                permutation(numbers[0:i]+numbers[i+1:], path + [numbers[i]])
        
        nums.sort()

        permutation(nums, [])
        return res


