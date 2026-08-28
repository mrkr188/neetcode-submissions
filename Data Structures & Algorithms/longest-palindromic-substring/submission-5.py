class Solution:
    def longestPalindrome(self, s: str) -> str:

        N = len(s)
        def expand_around_center(left, right):
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
            # when while condition fails we'd do left -= 1 and right += 1 to correct left, right
            return right - left - 1
        
        max_len = 0
        start = 0
        for i in range(N):

            # odd length palindromes (single character center)
            len1 = expand_around_center(i, i)
            # even length palindromes (between two characters)
            len2 = expand_around_center(i, i+1)

            curr_max = max(len1, len2)
            if curr_max > max_len:
                max_len = curr_max
                start = i - (curr_max - 1) // 2

        return s[start : start+max_len]
        

