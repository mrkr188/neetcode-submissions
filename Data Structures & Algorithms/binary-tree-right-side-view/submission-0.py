# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        queue = [root]
        
        while queue:
            res.append([node.val for node in queue][-1])
            queue = [child for i in queue if i for child in (i.left, i.right) if child]
        return res