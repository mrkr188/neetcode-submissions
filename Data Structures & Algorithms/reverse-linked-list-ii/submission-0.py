# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head

        for _ in range(left - 1):
            curr = curr.next
            leftPrev = leftPrev.next
        
        prev = None
        newTail = leftPrev.next
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        newTail.next = curr
        leftPrev.next = prev

        return dummy.next



        