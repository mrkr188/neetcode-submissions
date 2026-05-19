# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        stack = []
        node1 = node2 = prev = None
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if prev and prev.val > curr.val:
                node2 = curr
                if not node1:
                    node1 = prev
                else:
                    break
            prev = curr
            curr = curr.right

        node1.val, node2.val = node2.val, node1.val

