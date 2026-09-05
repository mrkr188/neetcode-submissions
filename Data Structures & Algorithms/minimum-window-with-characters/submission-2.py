class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count, window = {}, {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        needCount = len(count.keys())
        currCount = 0
        minLen = math.inf
        start, end = 0, 0
        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1
            if c in count and window[c] == count[c]:
                currCount += 1

            while currCount == needCount:
                if r-l+1 < minLen:
                    minLen = r-l+1
                    start, end = l, r
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    currCount -= 1
                l += 1
        
        return s[start:end+1] if minLen != math.inf else ""


        