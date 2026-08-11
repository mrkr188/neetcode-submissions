class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(path, left, right):
            if left == right == n:
                res.append(path)
            else:
                if left < n:
                    helper(path+'(', left+1, right)
                if right < left:
                    helper(path+')', left, right+1)
        helper('', 0, 0)
        return res


