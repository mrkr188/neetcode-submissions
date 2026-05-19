class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Track the longest palindrome found
        start = 0
        max_len = 0
        
        # Check each possible center
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            len1 = self.expand_around_center(s, i, i)
            # Even length palindromes (between two characters)
            len2 = self.expand_around_center(s, i, i + 1)
            
            # Get the longer palindrome
            current_len = max(len1, len2)
            
            # Update if we found a longer palindrome
            if current_len > max_len:
                max_len = current_len
                # Calculate start position of palindrome
                start = i - (current_len - 1) // 2
        
        # Extract and return the longest palindrome
        return s[start:start + max_len]

    # Helper function to expand around center
    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return length of palindrome
        return right - left - 1
        

