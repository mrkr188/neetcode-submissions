class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        m = 0
        # when we check nums[m] == 2, we'd do r -= 1, and swap the value at r to m position
        # we'd then have to check the element at m, so we have to make m <= r for that to happen
        while m <= r:
            if nums[m] == 0:
                nums[m] = nums[l]
                nums[l] = 0
                m += 1
                l += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m] = nums[r]
                nums[r] = 2
                r -= 1


        