# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        res = []
        node = root
        
        while node or stack:

            # reach the leftmost node of current subtree
            while node:
                stack.append(node)
                node = node.left

            # visit node: process the leftmost unvisited node
            node = stack.pop()
            res.append(node.val)

            # move to right child/subtree
            node = node.right

        return res
        