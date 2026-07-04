class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1]*n
        
        for i in range(1, n):
            answer[i] = answer[i-1]*nums[i-1]
        
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] = answer[i]*right
            right *= nums[i]
        
        return answer

        # n = len(nums)
        # res = [1] * n
        # pref = [1] * n
        # suff = [1] * n

        # for i in range(1, n):
        #     pref[i] = nums[i - 1] * pref[i - 1]
        # for i in range(n - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
            
        # for i in range(n):
        #     res[i] = pref[i] * suff[i]
        # return res