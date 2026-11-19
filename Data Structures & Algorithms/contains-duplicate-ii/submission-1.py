class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map = {}
        for i, num in enumerate(nums):
            if num in map:
                if i - map[num] <= k:
                    return True
            map[num] = i
        return False

        # window = set()
        # l = 0
        # for r in range(len(nums)):
        #     if r - l > k:
        #         window.remove(nums[l])
        #         l += 1
        #     if nums[r] in window:
        #         return True
        #     window.add(nums[r])
        # return False

        
