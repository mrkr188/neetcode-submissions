class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lastIndex = {c: i for i, c in enumerate(s)}
        
        res = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            # extend the current partition's end to the furthest last occurrence seen so far
            end = max(end, lastIndex[c])
            
            # if our current index matches the required end, we've found a complete partition
            if i == end:
                res.append(end - start + 1)
                start = i + 1  # move the start pointer to the next partition
                
        return res