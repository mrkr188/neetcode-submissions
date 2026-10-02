class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        # track max walls from both ends
        left_max, right_max = height[l], height[r]
        total = 0

        while l < r:
            # left wall is taller, so right side is the bottleneck
            if left_max > right_max:
                r -= 1
                right_max = max(right_max, height[r])
                total += right_max - height[r]
            # right wall is taller or equal, so left side is the bottleneck
            else:
                l += 1
                left_max = max(left_max, height[l])
                total += left_max - height[l]

        return total