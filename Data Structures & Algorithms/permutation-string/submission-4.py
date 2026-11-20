class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        matches = 0
        for c1, c2 in zip(s1, s2):
            s1Count[ord(c1) - ord('a')] += 1
            s2Count[ord(c2) - ord('a')] += 1
        
        matches = sum([s1Count[i] == s2Count[i] for i in range(26)])

        l = 0
        for r in range(l1, l2):
            if matches == 26:
                return True

            ix = ord(s2[r]) - ord('a')
            s2Count[ix] += 1

            if s2Count[ix] == s1Count[ix]:
                matches += 1
            if s2Count[ix] - 1 == s1Count[ix]:
                matches -= 1

            ix = ord(s2[l]) - ord('a')
            s2Count[ix] -= 1
            if s2Count[ix] == s1Count[ix]:
                matches += 1
            if s2Count[ix] + 1 == s1Count[ix]:
                matches -= 1
            
            l += 1
        
        return matches == 26


