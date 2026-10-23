"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:

    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):
            # base case: 1x1 grid is a leaf node
            if n == 1:
                return Node(grid[r][c] == 1, True)

            mid = n // 2
            # recursively divide into four equal quadrants
            topLeft = dfs(mid, r, c)
            topRight = dfs(mid, r, c + mid)
            bottomLeft = dfs(mid, r + mid, c)
            bottomRight = dfs(mid, r + mid, c + mid)

            # collapse into a single leaf if all four children are uniform leaves
            if (
                topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
                and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val
            ):
                return Node(topLeft.val, True)

            # otherwise, return an internal non-leaf node linking the four quadrants
            return Node(
                False, False, topLeft, topRight, bottomLeft, bottomRight
            )

        return dfs(len(grid), 0, 0)

