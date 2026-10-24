# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        cache = { None : 0 }

        def dfs(root):
            if root in cache:
                return cache[root]
            
            cache[root] = root.val
            if root.left:
                cache[root] += dfs(root.left.right) + dfs(root.left.left)
            if root.right:
                cache[root] += dfs(root.right.right) + dfs(root.right.left)
            
            cache[root] = max(cache[root], dfs(root.left) + dfs(root.right))
            return cache[root]
        
        return dfs(root)

        