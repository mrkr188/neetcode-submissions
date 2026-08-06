# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        stack = []
        node = root
        last = None
        max_sum = -math.inf
        paths = {None: 0} # node: max path sum with node as root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            peek = stack[-1]
            # right side of peek not processed
            if peek.right and peek.right != last:
                node = peek.right
            # both left and right for popped node are processed
            else:

                leftMax = max(paths[peek.left], 0)
                rightMax = max(paths[peek.right], 0)
                # update single side path max and store in paths dict
                paths[peek] = peek.val + max(leftMax, rightMax)

                # calcualte sum when we split at node
                node_split_sum = peek.val + leftMax + rightMax
                max_sum = max(max_sum, node_split_sum)

                stack.pop()
                last = peek
        return max_sum

        # res = [root.val]

        # def dfs(root):
        #     if not root:
        #         return 0

        #     leftMax = dfs(root.left)
        #     rightMax = dfs(root.right)
        #     leftMax = max(leftMax, 0)
        #     rightMax = max(rightMax, 0)

        #     res[0] = max(res[0], root.val + leftMax + rightMax)
        #     return root.val + max(leftMax, rightMax)

        # dfs(root)
        # return res[0]