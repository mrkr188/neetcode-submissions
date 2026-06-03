# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        stack = []
        pre = None
        depths = {None: 0} # node -> depth

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack[-1]
                # if there is no right child, or we just processed the right child
                if root.right == None or root.right == pre:
                    # retrieve the heights of the left and right subtrees
                    left_height = depths[root.left]
                    right_height = depths[root.right]
                    
                    # check for imbalance
                    if abs(left_height - right_height) > 1:
                        return False
                    
                    # cache the current node's height
                    depths[root] = 1 + max(left_height, right_height)
                    
                    # standard postorder movement
                    pre = stack.pop()
                    root = None
                else:
                    root = root.right
                    
        return True

        # def dfs(root):
        #     if not root:
        #         return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        #     return [balanced, 1 + max(left[1], right[1])]

        # return dfs(root)[0]




