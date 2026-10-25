# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = [root]
        result = deque()

        while stack:
            curr = stack.pop()
            # Prepend to the deque to reverse Root-Right-Left into Left-Right-Root
            result.appendleft(curr.val)

            # Push left first so right is popped and processed first
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return list(result)

        # if not root:
        #     return []
        
        # res = []
        # stack = []
        # node = root
        # # tracks last processed node to know if right subtree is done
        # prev = None
        # while stack or node:
        #     # reach the leftmost node of current subtree
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     peek = stack[-1]
        #     # move to right child if it exists and wasn't just visited
        #     if peek.right and peek.right != prev:
        #         node = peek.right
        #     # left and right subtrees are done: process current node
        #     else:
        #         res.append(peek.val)
        #         prev = stack.pop()
        # return res

            
        