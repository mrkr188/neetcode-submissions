# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(node, k):
            curr = node
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            
            if count < k:
                return node, None, None
                
            new_tail = node
            new_head = None
            next_node = node

            while k and next_node:
                tmp = next_node.next
                next_node.next = new_head
                new_head = next_node
                next_node = tmp
                k -= 1
            return new_head, new_tail, next_node

        new_head, prev_tail, next_node = reverse(head,k)
        res = new_head
        
        while next_node:
            new_head, new_tail, next_node = reverse(next_node,k)
            prev_tail.next = new_head
            prev_tail = new_tail
        return res