class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        mp = {}
        l, r = 0, 0
        maxLen = 0
        for r in range(len(s)):
            if s[r] in mp:
                # ensure 'l' only moves forward
                l = max(mp[s[r]]+1, l)
            maxLen = max(maxLen, r-l+1)
            mp[s[r]] = r
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