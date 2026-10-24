# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rob(self, root: Optional[TreeNode]) -> int:

        cache = {None: 0}

        def dfs(root):
            # return cached result if we've already computed this node
            if root in cache:
                return cache[root]

            # option 1: rob the current node
            # we get root.val plus the money from its 4 grandchildren (skipping direct children)
            val = root.val
            if root.left:
                val += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                val += dfs(root.right.left) + dfs(root.right.right)

            # option 2: skip the current node
            # we take the max money from its left child and right child instead
            skip = dfs(root.left) + dfs(root.right)

            # store the best choice between robbing or skipping this node
            cache[root] = max(val, skip)
            return cache[root]

        return dfs(root)