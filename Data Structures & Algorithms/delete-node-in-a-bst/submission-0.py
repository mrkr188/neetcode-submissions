# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        
        curr = root
        if curr.val > key:
            curr.left = self.deleteNode(curr.left, key)
        elif curr.val < key:
            curr.right = self.deleteNode(curr.right, key)
        else:
            if not curr.right:
                return curr.left
            if not curr.left:
                return curr.right
            
            min_node = curr.right
            while min_node.left:
                min_node = min_node.left
            curr.val = min_node.val
            curr.right = self.deleteNode(curr.right, min_node.val)
        
        return root
            



        