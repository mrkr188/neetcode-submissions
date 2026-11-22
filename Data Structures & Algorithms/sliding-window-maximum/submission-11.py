class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        # store indices of elements in monotonically decreasing order
        queue = deque()

        for r, val in enumerate(nums):
            # remove elements smaller than current val from the back
            while queue and nums[queue[-1]] < val:
                queue.pop()
            
            # add current index
            queue.append(r)

            # remove indices that fall outside the current sliding window [r - k + 1, r]
            if queue[0] < r - k + 1:
                queue.popleft()

            # record the maximum (front of queue) once the first window of size k is reached
            if r >= k - 1:
                res.append(nums[queue[0]])

        return res