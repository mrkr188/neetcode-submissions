# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        stack = [root]
        res = 0
        mp = { None : (0, 0) } # node: height, diameter 
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()

                l_h, l_d = mp[node.left]
                r_h, r_d = mp[node.right]

                mp[node] = (1 + max(l_h, r_h), max(l_h + r_h, l_d, r_d))
        return mp[root][1]

    #   def dfs(node):
    #       if not node:
    #           return 0, 0  # height, diameter
    #       l_h, l_d = dfs(node.left)
    #       r_h, r_d = dfs(node.right)
    #       return 1 + max(l_h, r_h), max(l_h + r_h, l_d, r_d)

    #   return dfs(root)[1]

