class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # search in right half (lower half)
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

            # search in left half (higher half)
            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            # if nums[r] == nums[m] we don't know where to search, so decrement r
            else:
                r -= 1
        return -1



