class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-k   # r is a valid window-start, kept in range
        while l<r:
            m = l + (r-l)//2
            if x - arr[m] <= arr[m+k] - x: 
                r = m     # m is still a candidate start -> keep it
            else:
                l = m+1
        return arr[l:l + k] # l == r == best start
