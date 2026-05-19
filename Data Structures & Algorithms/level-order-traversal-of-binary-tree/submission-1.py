# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []

        # q = collections.deque()
        # q.append(root)

        # while q:
        #     qLen = len(q)
        #     level = []
        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         res.append(level)

        # return res

        levels = []
        if not root:
            return levels
        
        queue = [root]
        level = 0
        
        while queue:
            levels.append([])
            levels[level] = [node.val for node in queue]
            queue = [child for i in queue if i for child in (i.left, i.right) if child]
            level += 1
        return levels






        