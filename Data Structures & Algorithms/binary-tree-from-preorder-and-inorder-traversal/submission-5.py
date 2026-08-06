# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        # return root
        
        # we construct tree in order of preorder nodes
        pre_iter = iter(preorder)

        # by constructing this map we look up root node in inorder in O(1)
        inirder_map = { v:i for i,v in enumerate(inorder) }

        def helper(left, right):

            if left > right:
                return None
            
            root_val = next(pre_iter)
            root = TreeNode(root_val)

            mid = inirder_map[root_val]

            # node at mid is already added to tree
            # in next recursion, we exclude it and continue
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)

            return root
        
        # recursively call this till we add all node sin preorder to tree and return root
        return helper(0, len(preorder)-1)

