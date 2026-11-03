class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)
        if total % k != 0:
            return False
        
        sum_needed = total / k
        nums.sort(reverse = True)
        if sum_needed < nums[0]:
            return False
        
        buckets = [0] * k
        def backtrack(idx):
            if idx == len(nums):
                return all(bucket == sum_needed for bucket in buckets)
            
            for i in range(k):
                if buckets[i] + nums[idx] <= sum_needed:
                    buckets[i] += nums[idx]
                    if backtrack(idx + 1):
                        return True
                    buckets[i] -= nums[idx]

                    if buckets[i] == 0:
                        break
            return False
        return backtrack(0)
                    
        