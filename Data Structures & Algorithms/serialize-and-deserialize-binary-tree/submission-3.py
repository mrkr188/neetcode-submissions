# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        if not root:
            return 'N'

        stack = [root]
        res = []
        while stack:

            node = stack.pop()
            if not node:
                res.append('N')
            else:
                res.append(str(node.val))

                stack.append(node.right)
                stack.append(node.left)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        tree_list = data.split(',')[::-1]
        # print(tree_list)

        def helper():
            root_val = tree_list.pop()
            if root_val == 'N':
                return None

            root = TreeNode(int(root_val))
            root.left = helper()
            root.right = helper()
            return root

        return helper()


