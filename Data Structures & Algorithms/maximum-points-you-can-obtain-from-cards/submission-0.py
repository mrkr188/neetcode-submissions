class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:

        curr_sum = sum(cards[:k])
        res = curr_sum

        for i in range(1, k+1):
            curr_sum += cards[-i] - cards[k-i]
            res = max(res, curr_sum)
        return res

        