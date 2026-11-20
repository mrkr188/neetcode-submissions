class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = {}
        l = 0
        maxLen = 0
        for r, c in enumerate(s):
            if c in mp:
                # ensure 'l' only moves forward
                l = max(mp[c] + 1, l)
            maxLen = max(maxLen, r-l+1)
            mp[c] = r
        return maxLen

        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res