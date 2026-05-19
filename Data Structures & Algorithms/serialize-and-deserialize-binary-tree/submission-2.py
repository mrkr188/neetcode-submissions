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

        left = self.serialize(root.left)
        right = self.serialize(root.right)

        # print(str(root.val) + ',' + left + ',' + right)        
        return str(root.val) + ',' + left + ',' + right

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


