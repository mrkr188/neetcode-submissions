class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Rotated Array: [4, 5, 6, 7, 0, 1, 2]
        #      |________|  |______|
        #       High Half   Low Half
        # When an array is sorted and rotated, it splits into two distinct sorted halves: a High half # and a Low half. The minimum element is the very first element of the Low half.

        # Case 1
        # intution - if nums[m] < nums[r] then we can conclude that right side is increasing 
        # so we can conclude no element there would be greater than nums[m], so we can limit search to r = m

        # Case 2
        # if nums[m] > nums[r] we know that the influx point is somewhere to the right side so we choose l = m+1

        # Case 3
        # if nums[m] == nums[r], this is blind spot, we don't know which part of array to search.
        # so we decrement r by 1

        # as our search narrows down we get min point when l and r converge
        # note here we can't use r = m-1 because we'd not be comparing the element at m with rest of the elements 

        l,r = 0,len(nums)-1
        while r > l:
            m = l + (r - l)//2
            # case 1):
            if nums[m] < nums[r]:
                r = m 
            # case 2):
            elif nums[m] > nums[r]:
                l = m + 1
            # case 3):
            else:
                r -= 1
        # the 'l' and 'r' index converge to the inflection point.
        return nums[r]