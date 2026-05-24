class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0
        l = 0
        maxFreq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])

            if (r-l+1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
            
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
            