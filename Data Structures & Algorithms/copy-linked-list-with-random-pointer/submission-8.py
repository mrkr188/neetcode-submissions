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

        # 1st pass - add new nodes adjacent to old nodes
        l1 = head
        while l1:
            l2 = Node(l1.val)
            temp = l1.next
            l1.next = l2
            l2.next = temp
            l1 = temp

        # 2nd pass - update random nodes 
        l1 = head
        while l1:
            if l1.random:
                l1.next.random = l1.random.next
            l1 = l1.next.next

        # 3rd pass - remove connections
        # A->A'->B->B'->C->C' to A->B->C and A'->B'->C'
        newHead = head.next
        l1 = head
        while l1:
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead






