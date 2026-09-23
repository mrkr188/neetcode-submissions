# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stack = []
        node = root
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            peek = stack[-1]
            if peek.right and peek.right is not prev:
                node = peek.right
            else:
                res.append(peek.val)
                prev = stack.pop()
        return res

            
        