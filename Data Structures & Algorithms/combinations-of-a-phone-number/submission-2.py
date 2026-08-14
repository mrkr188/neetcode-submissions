class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
            
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        n = len(digits)
        res = []
        
        def helper(path, index, k):
            if k == n:
                res.append(path)
            else:
                chars = d[digits[index]]
                for i in range(len(chars)):
                    helper(path+chars[i], index+1, k+1)
        
        helper('', 0, 0)
        return res


