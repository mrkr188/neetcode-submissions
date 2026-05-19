class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if not str:
            return str
        
        stack = []
        

        for portion in path.split("/"):
            
            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                stack.append(portion)
            
        final_str = "/" + "/".join(stack)
        return final_str 