class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []

        # l, r = 0, len(numbers) - 1

        # while l < r:
        #     curSum = numbers[l] + numbers[r]

        #     if curSum > target:
        #         r -= 1
        #     elif curSum < target:
        #         l += 1
        #     else:
        #         return [l + 1, r + 1]
        # return []