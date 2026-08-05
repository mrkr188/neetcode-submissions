# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diameter = 0
        stack = []
        depths = {None: 0} # node -> depth
        node = root
        last = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            peek = stack[-1]
            # right subtree not done yet -> go right
            if peek.right and peek.right != last:
                node = peek.right
            # both children done -> process node
            else:
                left_depth = depths[peek.left]
                right_depth = depths[peek.right]

                # update the max diameter found so far
                max_diameter = max(max_diameter, left_depth+right_depth)
                # cache the current node's height
                depths[peek] = 1+max(left_depth, right_depth)

                last = peek
                stack.pop()

        return max_diameter


    #   def dfs(node):
    #       if not node:
    #           return 0, 0  # height, diameter
    #       l_h, l_d = dfs(node.left)
    #       r_h, r_d = dfs(node.right)
    #       return 1 + max(l_h, r_h), max(l_h + r_h, l_d, r_d)

    #   return dfs(root)[1]

