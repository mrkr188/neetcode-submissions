class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # step 1: replace -ve numbers with 0
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        # step 2: use -ve signs as presence markers
        for i in range(n):
            val = abs(nums[i]) - 1
            if 0 <= val < n: 
                # mark index val as "seen" by making the number negative
                # -0 is still 0, so use a dummy negative number instead
                if nums[val] == 0:
                    nums[val] = -(n + 1)  
                # flip positive to negative so we know the number exists
                elif nums[val] > 0:
                    nums[val] = -nums[val]  
        
        # step 3: return the first index that isn't marked negative
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i
        
        return n + 1
