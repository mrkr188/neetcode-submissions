class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        length = mountainArr.length()
        l, r = 1, length - 2
        pivot = 1
        while l <= r:
            m = (r - l)//2 + l
            # peak at m or left, save m and move left
            # we don't need to check m == lenght - 1, because we're told array length >= 3
            # and the array is a mountain array 
            if mountainArr.get(m) > mountainArr.get(m+1):
                pivot = m
                r = m - 1
            else:
                l = m + 1
        
        # check left
        l, r = 0, pivot
        while l <= r:
            m = (r - l)//2 + l
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid < target:
                l = m + 1
            else:
                r = m - 1
        
        # check right
        l, r = pivot, length - 1
        while l <= r:
            m = (r - l)//2 + l
            mid = mountainArr.get(m)
            if mid == target:
                return m
            elif mid > target:
                l = m + 1
            else:
                r = m - 1
        
        return -1




        