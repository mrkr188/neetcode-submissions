class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        # half target size; for odd total length, right side holds 1 extra element
        half = total // 2

        # binary search on smaller array to guarantee o(log(min(m, n)))
        if len(B) < len(A):
            A, B = B, A

        # search range over A's indices
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2

            # why j = half - i - 2?
            # i and j are 0-based indices, so A contributes (i + 1) elements
            # and B contributes (j + 1) elements to the left partition.
            # total left elements needed = half:
            # (i + 1) + (j + 1) = half  =>  i + j + 2 = half  =>  j = half - i - 2
            j = half - i - 2

            # safe placeholders for empty partitions / out of bounds elements
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # valid partition: all left numbers <= all right numbers
            if Aleft <= Bright and Bleft <= Aright:
                # odd total length: take smallest from right side
                # this is ebcause right side holds 1 extra element
                if total % 2:
                    return min(Aright, Bright)
                # even total length: average of max-left and min-right
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aright < Bleft:
                # A's left partition is too small, move right
                l = i + 1
            else:
                # A's left partition is too large (Aleft > Bright), move left
                r = i - 1

