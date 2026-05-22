class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = [0] * 26
        for i, j in zip(s, t):
            count[ord(i) - ord('a')] += 1
            count[ord(j) - ord('a')] -= 1
        
        return all(val == 0 for val in count)

