# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node, k):
            check = node
            count = 0
            while check and count < k:
                check = check.next
                count += 1
            
            if count < k:
                return node, None, None
                
            tail = node
            prev = None

            while k and node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
                k -= 1
            return prev, tail, node

        new_head, prev_tail, next_node = reverse(head,k)
        res = new_head
        
        while next_node:
            new_head, new_tail, next_node = reverse(next_node,k)
            prev_tail.next = new_head
            prev_tail = new_tail
        return res