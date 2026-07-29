class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # l, r = 0, len(arr)-k-1
        # while l<=r:
        #     m = l + (r-l)//2
        #     if x - arr[m] <= arr[m+k] - x:
        #         r = m-1
        #     else:
        #         l = m+1
        # return arr[l:l + k]

        l, r = 0, len(arr) - k - 1         # r is a valid window-start, kept in range
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                ans = m + 1
                l = m + 1
            else:
                r = m - 1                # m is still a candidate start -> keep it
        return arr[ans:ans + k]                         # l == r == best start