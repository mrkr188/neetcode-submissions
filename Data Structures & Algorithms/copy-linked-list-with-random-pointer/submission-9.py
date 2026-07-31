"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        curr = head
        # A -> A' -> B -> B'
        while curr:
            newNode = Node(curr.val)
            tmp = curr.next
            curr.next = newNode
            newNode.next = tmp
            curr = tmp

        # add random nodes to newNodes
        curr = head
        while curr and curr.next:
            oldNode = curr
            newNode = curr.next
            if oldNode.random:
                newNode.random = oldNode.random.next
            curr = curr.next.next
        
        # A -> B and A' -> B'
        curr = head
        newHead = head.next
        while curr and curr.next:
            oldNode = curr
            newNode = curr.next
            curr = curr.next.next
            oldNode.next = newNode.next
            if newNode.next:
                newNode.next = newNode.next.next
        return newHead


