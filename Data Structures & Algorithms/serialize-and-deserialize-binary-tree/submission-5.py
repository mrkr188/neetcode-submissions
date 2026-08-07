class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(res)

        # preorder
        # if not root:
        #     return 'N'
        
        # stack = [root]
        # res = []
        # while stack:
        #     node = stack.pop()
        #     if not node:
        #         res.append('N')
        #     else:
        #         res.append(str(node.val))
        #         stack.append(node.right)
        #         stack.append(node.left)
        # return ','.join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(',')
        if vals[0] == 'N':
            return None
        
        i = 1
        root = TreeNode(vals[0])
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if vals[i] != 'N':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i]!= 'N':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
