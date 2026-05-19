class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # s = set()
        # for n in nums:
        #     if n in s:
        #         s.remove(n)
        #     else:
        #         s.add(n)
        # return s.pop()
        
        # using bitwise
        a = 0
        for n in nums:
            a ^= n
        return a