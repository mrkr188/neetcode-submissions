class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        n = len(height)
        # track max walls from both ends
        left_max, right_max = height[0], height[n - 1]

        l, r = 1, n-2
        total = 0

        while l <= r:
            # left wall is taller, so right side is the bottleneck
            if left_max > right_max:
                right_max = max(right_max, height[r])
                total += right_max - height[r]
                r -= 1
            # right wall is taller or equal, so left side is the bottleneck
            else:
                left_max = max(left_max, height[l])
                total += left_max - height[l]
                l += 1

        return total
