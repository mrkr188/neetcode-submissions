# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head

        # advance pointers so curr is at position left and leftPrev is right before left
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
        
        # connect sublist tail to the remaining nodes after position right
        newTail.next = curr
        # connect node before position left to the new head of the reversed sublist
        leftPrev.next = prev

        return dummy.next



        