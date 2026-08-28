class Solution:
    def numDecodings(self, s: str) -> int:

        N = len(s)
        # for empty string N = 0, num decodings = 1
        # store num decodings at index s[i:]
        dp = { N: 1 }

        for i in range(N-1, -1, -1):

            if s[i] == '0':
                dp[i] = 0
                continue
            
            dp[i] = dp[i+1]

            if i + 1 < N and \
                (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                dp[i] += dp[i+2]
        
        return dp[0]
        