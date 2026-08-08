import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(nums, left, right):
            lt = left
            i = left
            gt = right
            p = random.randint(left, right)
            nums[p], nums[right] = nums[right], nums[p]
            pivot = nums[right]
            # at each index i we compare with nums[i] with pivot 
            #  [--- less --> lt <-- equal --> gt <-- greater --]
            while i <= gt:
                # less than pivot, move to start of array
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    i += 1
                    lt += 1
                # greater than pivot, move to end of array
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    # don't advance i: swapped-in value at gt is unseen
                    gt -= 1
                # same as pivot, just move i to i+1
                else:
                    i += 1
            return lt, gt
        
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            lt, gt = partition(nums, left, right)
            if target < lt:
                right = lt - 1
            elif target > gt:
                left = gt + 1
            else:
                return nums[target]

        # pivot = random.choice(nums)

        # left, mid, right = [], [], []
        # for num in nums:
        #     if num > pivot:
        #         right.append(num)
        #     elif num < pivot:
        #         left.append(num)
        #     else:
        #         mid.append(num)

        # # this means kth largest element should be right side
        # if k <= len(right):
        #     return self.findKthLargest(right, k)
        # # this means kth largest element should be left side
        # elif len(right) + len(mid) < k:
        #     return self.findKthLargest(left, k - len(mid) - len(right))

        # return pivot

        # good when k << n
        # minHeap = []
        # for num in nums:
        #     heapq.heappush(minHeap, num)
        #     if k < len(minHeap):
        #         heapq.heappop(minHeap)
        # return minHeap[0]

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




