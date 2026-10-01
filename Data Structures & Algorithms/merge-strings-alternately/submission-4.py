class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # l, r = 0, 0
        # res = []
        # while l < len(word1) and r < len(word2):
        #     res.append(word1[l])
        #     res.append(word2[r])
        #     l += 1
        #     r += 1
        # res.append(word1[l:])
        # res.append(word2[r:])
        # return "".join(res)

        l1, l2 = len(word1), len(word2)
        
        res = []
        for c1, c2 in zip(word1, word2):
            res += [c1, c2]
        
        return ''.join(res) + (word2[l1:] if l2 > l1 else word1[l2:])
            