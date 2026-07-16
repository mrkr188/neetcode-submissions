class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0
        l = 0
        maxFreq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])

            # if (length of window) - (max count of a char) > k
            # move start by 1. remove count of start char
            if (r-l+1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

            # window never actually gets smaller than its best — it either grows or slides.
            # But what if I removed the dominant char?"
            # Doesn't matter. Even if the true max is now lower, we keep the stale maxFreq. 
            # The window just stays the same size and keeps sliding. It won't grow (and won't update res) 
            # until r finds a char that actually pushes maxFreq higher. 
            # So no wrong answer is ever recorded — we just slide until we find something better.
            
        return res

        # res = 0
        # charSet = set(s)

        # for c in charSet:
        #     count = l = 0
        #     for r in range(len(s)):
        #         if s[r] == c:
        #             count += 1

        #         while (r - l + 1) - count > k:
        #             if s[l] == c:
        #                 count -= 1
        #             l += 1

        #         res = max(res, r - l + 1)
        # return res
            