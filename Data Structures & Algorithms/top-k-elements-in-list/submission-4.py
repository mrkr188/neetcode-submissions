class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        
        # Create a list of tuples with negative frequencies for a max-heap effect
        # Format: [(-frequency, element), ...]
        heap = [(-freq, num) for num, freq in count.items()]
        
        # Transform list into a heap in-place: O(N)
        heapq.heapify(heap)
        
        # Pop the k smallest (most negative) elements: O(k log N)
        result = []
        for _ in range(k):
            # heappop always returns the smallest element
            freq, num = heapq.heappop(heap)
            result.append(num)
            
        return result

        # heap solution
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]



        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # for num, cnt in count.items():
        #     freq[cnt].append(num)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res





