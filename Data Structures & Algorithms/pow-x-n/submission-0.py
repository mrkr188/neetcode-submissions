class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1: 
            return x
        
        res = 1
        power = abs(n)

        while power:
            if power & 1:
                res *= x
            x *= x
            power >>= 1

        return res if n >= 0 else 1 / res
    
 