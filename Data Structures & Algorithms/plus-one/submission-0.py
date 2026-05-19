class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        carry = 1
        while n >= 0:
            carry += digits[n]
            digits[n] = carry%10
            carry //= 10
            n -= 1
        if carry:
            return [carry] + digits
        return digits