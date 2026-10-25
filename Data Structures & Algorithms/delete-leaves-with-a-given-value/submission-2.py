# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        stack = []
        prev = None
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            peek = stack[-1]
            if peek.right and peek.right != prev:
                node = peek.right
                continue
            
            curr = stack.pop()
            if not curr.left and not curr.right and curr.val == target:
                # if the entire tree is just a single target leaf, return None
                if not stack:
                    return None
                
                # popping curr exposes the node right below it, so curr's parent is stack[-1]
                # detach the leaf from its parent
                parent = stack[-1]
                if parent.left == curr:
                    parent.left = None
                if parent.right == curr:
                    parent.right = None
                
            else:
                prev = curr
        
        return root

        # # base case: empty node
        # if not root:
        #     return None

        # # recursively process left and right subtrees first (post-order)
        # root.left = self.removeLeafNodes(root.left, target)
        # root.right = self.removeLeafNodes(root.right, target)

        # # if current node became a target leaf after its children were removed, delete it
        # if not root.left and not root.right and root.val == target:
        #     return None

        # return root
                

        