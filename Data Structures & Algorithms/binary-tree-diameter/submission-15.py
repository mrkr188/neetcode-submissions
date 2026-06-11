# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        stack = []
        pre = None
        depths = {None: 0} # node -> depth
        max_diameter = 0

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                # if there is no right child, or we just processed the right child
                if root.right == None or root.right == pre:
                    left_height = depths[root.left]
                    right_height = depths[root.right]
                    
                    # ipdate the max diameter found so far
                    max_diameter = max(max_diameter, left_height + right_height)
                    
                    # cache the current node's height
                    depths[root] = 1 + max(left_height, right_height)
                    
                    # standard postorder movement
                    pre = stack.pop()
                    root = None
                else:
                    root = root.right
                    
        return max_diameter

    #   def dfs(node):
    #       if not node:
    #           return 0, 0  # height, diameter
    #       l_h, l_d = dfs(node.left)
    #       r_h, r_d = dfs(node.right)
    #       return 1 + max(l_h, r_h), max(l_h + r_h, l_d, r_d)

    #   return dfs(root)[1]

