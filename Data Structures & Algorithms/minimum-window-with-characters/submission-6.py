class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l1, l2 = len(s), len(t)
        if l1 < l2:
            return ""
        
        need, window = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        needCount = len(need)
        currCount = 0

        minLen = math.inf
        res = ""

        l, r = 0, 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in need and need[c] == window[c]:
                currCount += 1
            
            while currCount == needCount:
                if minLen > r - l + 1:
                    minLen = r - l + 1
                    res = s[l : r + 1]

                window[s[l]] -= 1
                if s[l] in need and window[s[l]] == need[s[l]] - 1:
                    currCount -= 1
                l += 1

        return res


        