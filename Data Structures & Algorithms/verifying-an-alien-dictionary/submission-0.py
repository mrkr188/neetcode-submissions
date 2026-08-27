class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_ix = { c: i for i,c in enumerate(order) }

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]

            for i in range(len(w1)):
                if i == len(w2):
                    return False

                if w1[i] != w2[i]:
                    if order_ix[w1[i]] > order_ix[w2[i]]:
                        return False
                    break
        return True
