# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        stack = []
        prev = None
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            peek = stack[-1]
            if peek.right and peek.right != prev:
                node = peek.right
                continue
            
            curr = stack.pop()
            if not curr.left and not curr.right and curr.val == target:
                if not stack:
                    return None
                
                parent = stack[-1]
                if parent.left == curr:
                    parent.left = None
                if parent.right == curr:
                    parent.right = None
                
            else:
                prev = curr
        
        return root
                

        