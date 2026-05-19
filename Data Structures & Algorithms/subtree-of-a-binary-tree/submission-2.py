# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False

    #     if self.sameTree(root, subRoot):
    #         return True
    #     return (self.isSubtree(root.left, subRoot) or
    #            self.isSubtree(root.right, subRoot))

    # def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not root and not subRoot:
    #         return True
    #     if root and subRoot and root.val == subRoot.val:
    #         return (self.sameTree(root.left, subRoot.left) and
    #                self.sameTree(root.right, subRoot.right))
    #     return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        t = self.nodeSerialization(root)
        s = self.nodeSerialization(subRoot)

        return s in t

    def nodeSerialization(self, root):
        if not root:
            return '#'
        
        res = ''
        res += '^'
        res += str(root.val)
        res += self.nodeSerialization(root.left)
        res += self.nodeSerialization(root.right)
        return res