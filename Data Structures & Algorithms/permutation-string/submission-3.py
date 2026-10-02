class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        n1, n2 = len(s1), len(s2)
        s1count = [0] * 26
        s2count = [0] * 26

        for i in range(n1):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        matches = sum([c1 == c2 for c1, c2 in zip(s1count, s2count)])

        for j in range(n1, n2):
            
            if matches == 26:
                return True

            index = ord(s2[j - n1]) - ord('a')
            s2count[index] -= 1

            if s2count[index] == s1count[index]:
                matches += 1
            if s2count[index] + 1 == s1count[index]:
                matches -= 1

            index = ord(s2[j]) - ord('a')
            s2count[index] += 1

            if s2count[index] == s1count[index]:
                matches += 1
            if s2count[index] - 1 == s1count[index]:
                matches -= 1
        
        return matches == 26


