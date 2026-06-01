# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # returns new_head, new_tail, next_head 
    def reverse(self, head, k):

        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head, None, None

        # prev is new tail
        # curr is next head
        # head we pass in will be new tail after reversing list
        new_tail = head
        prev = None
        curr = head

        # we stop of reversing k elements, since after we have more nodes after passing k elements
        while count and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count -= 1

        return prev, new_tail, curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        res, prev_tail, next_node = self.reverse(head, k)

        while next_node:
            new_head, new_tail, next_node = self.reverse(next_node, k)
            prev_tail.next = new_head
            prev_tail = new_tail
        
        return res

        
    

            