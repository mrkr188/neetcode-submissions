# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            # push right child first so left child is processed first (LIFO order)
            if node.right:
                stack.append(node.right)
            # push left child second so it sits on top of the stack
            if node.left:
                stack.append(node.left)
        return res