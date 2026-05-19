# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

      def dfs(node):
          if not node:
              return 0, 0  # height, diameter
          l_h, l_d = dfs(node.left)
          r_h, r_d = dfs(node.right)
          return 1 + max(l_h, r_h), max(l_h + r_h, l_d, r_d)

      return dfs(root)[1]

        # self.res = 0

        # def dfs(root):

        #     if not root:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     self.res = max(self.res, left + right)

        #     return 1 + max(left, right)

        # dfs(root)
        # return self.res
