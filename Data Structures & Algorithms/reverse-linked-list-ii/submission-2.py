# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head

        k = 1
        # advance pointers so curr is at position left and leftPrev is right before left
        while k < left:
            curr = curr.next
            leftPrev = leftPrev.next
            k += 1
        
        prev = None      # prev will be new head after loop
        newTail = curr   # new tail will be curr head
        while k <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k += 1
        
        # connect sublist tail to the remaining nodes after position right
        newTail.next = curr
        # connect node before position left to the new head of the reversed sublist
        leftPrev.next = prev

        return dummy.next



        