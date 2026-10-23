# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        stack = [(root, root.val)]
        count = 0
        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                count += 1
                max_val = node.val
            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))
        return count
        
        # res = 0
        # q = deque()

        # q.append((root, -math.inf))

        # while q:
        #     node, maxval = q.popleft()
        #     if node.val >= maxval:
        #         res += 1
            
        #     if node.left:
        #         q.append((node.left, max(node.val, maxval)))
        #     if node.right:
        #         q.append((node.right, max(node.val, maxval)))
        
        # return res

        # def dfs(node, maxVal):
        #     if not node:
        #         return 0

        #     res = 1 if node.val >= maxVal else 0
        #     maxVal = max(maxVal, node.val)
        #     res += dfs(node.left, maxVal)
        #     res += dfs(node.right, maxVal)
        #     return res

        # return dfs(root, root.val)
        