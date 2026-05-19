import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # return heapq.nlargest(k, nums)[-1]

        # def heapify(nums, n, i):
        #     left = 2*i + 1
        #     right = 2*i + 2
        #     largest = i
        #     if left < n and nums[i] < nums[left]:
        #         largest = left
        #     if right < n and nums[largest] < nums[right]:
        #         largest = right
        #     if i != largest:
        #         nums[largest], nums[i] = nums[i], nums[largest]
        #         heapify(nums, n, largest)
        
        # n = len(nums)
        # # create max heap
        # for i in range(n//2, -1, -1):
        #     heapify(nums, n, i)
        
        # # swap max element with last in array and heapify
        # for i in range(k-1):
        #     nums[0], nums[n-1-i] = nums[n-i-1], nums[0]
        #     heapify(nums, n-1-i, 0)
        
        # return nums[0]

        pivot = random.choice(nums)

        left, mid, right = [], [], []
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)

        if k <= len(left):
            return self.findKthLargest(left, k)
        elif len(left) + len(mid) < k:
            return self.findKthLargest(right, k - len(mid) - len(left))

        return pivot