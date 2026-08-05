# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        depths = {None: 0}
        stack = []
        node = root
        last = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            peek = stack[-1]
            # right side not processed, navigate right side
            if peek.right and peek.right != last:
                node = peek.right
            # left, right children processed for node. verify condition for node
            else:
                left_depth = depths[peek.left]
                right_depth = depths[peek.right]

                depths[peek] = 1 + max(left_depth, right_depth)

                if abs(left_depth - right_depth) > 1:
                    return False

                stack.pop()
                last = peek
        return True

        # def dfs(root):
        #     if not root:
        #         return [True, 0]

        #     left, right = dfs(root.left), dfs(root.right)
        #     balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        #     return [balanced, 1 + max(left[1], right[1])]

        # return dfs(root)[0]




