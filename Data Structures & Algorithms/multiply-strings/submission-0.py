class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                # ~i is bitwise operation = -(i+1)
                ans += ((ord(num1[~i]) - ord('0')) * 10 ** i) * ((ord(num2[~j]) - ord('0')) * 10 ** j) 
        return str(ans)



