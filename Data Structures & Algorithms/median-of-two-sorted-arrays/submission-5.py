class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        # for odd total array size, right side holds 1 more number
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            # assume total numbers on left for A and B i+1, j+1 
            # (since it's 0 index we will have +1 on left)
            # i+j+2 = half ==? j = half-i-2. 
            # again notice when odd array size, right side holds 1 more number
            i = (l + r) // 2
            j = half - i - 2

            # This acts as a safe placeholder - there's nothing on left of A to consider
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                # take smallest from right since right side will have more elements when odd
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1




