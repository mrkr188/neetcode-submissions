class Solution:
    def reverse(self, x: int) -> int:

        MIN, MAX = -0x7FFFFFFF, 0x7FFFFFFF
        res = 0
        
        # Work with the absolute value to keep logic simple
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = x % 10
            x //= 10

            # Overflow check
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            
            res = (res * 10) + digit

        return res * sign