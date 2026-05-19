class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in d.keys():
                if not stack or d[c] != stack.pop():
                    return False
            elif c in d.values():
                stack.append(c)
            else:
                return False
        return stack == []