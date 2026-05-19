class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def permutation(numbers, curr, result):
            if len(numbers) == 0:
                result.append(curr)

            for i in range(len(numbers)):
                if i > 0 and numbers[i] == numbers[i-1]:
                    continue
                permutation(numbers[0:i]+numbers[i+1:], curr + [numbers[i]], result)
        
        nums.sort()
        result = []
        permutation(nums, [],result)
        return result


