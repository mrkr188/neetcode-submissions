class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # l, r = 0, len(arr)-k   # r is a valid window-start, kept in range
        # while l<r:
        #     m = l + (r-l)//2
        #     if x - arr[m] <= arr[m+k] - x: 
        #         r = m     # m is still a candidate start -> keep it
        #     else:
        #         l = m+1
        # return arr[l:l + k] # l == r == best start

        l, r = 0, len(arr) - k - 1      # r is inclusive, so the last valid start is len(arr)-k-1
        idx = len(arr) - k              # default: the rightmost window
        while l <= r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1               # window m is too far left, discard it
            else:
                idx = m                 # m is a candidate start -> remember it
                r = m - 1               # ...and look for an even smaller one
        return arr[idx:idx + k]

