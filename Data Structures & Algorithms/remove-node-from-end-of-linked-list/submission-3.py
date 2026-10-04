# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        # advance curr pointer n steps ahead to create a gap of size n
        curr = head
        while n > 0:
            n -= 1
            curr = curr.next

        # move both curr and prev until curr reaches the end;
        # prev will then land right before the target node to delete 
        prev = dummy
        while curr:
            prev = prev.next
            curr = curr.next
        
        # remove nth node from end
        prev.next = prev.next.next
        return dummy.next

