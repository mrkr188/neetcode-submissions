"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node
        
        oldToNew = {}
        queue = deque([node])
        
        oldToNew[node] = Node(node.val, [])
        
        while queue:
            n = queue.popleft()
            
            for neighbor in n.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                oldToNew[n].neighbors.append(oldToNew[neighbor])
        
        return oldToNew[node]

        # oldToNew = {}
        # if not node:
        #     return node
        # def dfs(node):
        #     if node in oldToNew:
        #         return oldToNew[node]

        #     copy = Node(node.val)
        #     oldToNew[node] = copy
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))
        #     return copy

        # return dfs(node) if node else None



        