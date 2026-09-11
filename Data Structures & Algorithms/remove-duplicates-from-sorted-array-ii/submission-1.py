class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # l - where to place the next allowed number
        # r - where we are currently looking/scanning
        l, r = 0, 0

        while r < len(nums):
            # count consecutive duplicates for current number
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1

            # write at most 2 occurrences into the valid array
            for i in range(min(count, 2)):
                nums[l] = nums[r]
                l += 1

            # move r to start of next unique group
            r += 1

        return l  # l represents the length of updated array