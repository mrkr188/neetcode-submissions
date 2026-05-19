class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if not stack or closeToOpen[c] != stack.pop():
                    return False
            elif c in closeToOpen.values():
                stack.append(c)
            else:
                return False

        return True if not stack else False