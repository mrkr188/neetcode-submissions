class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return True

            # search left side of midpint
            if nums[m] > nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1

            # search right side of midpoint
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            # when nums[m] = nums[l], just move one pointer from left
            else:
                l += 1 
        return False