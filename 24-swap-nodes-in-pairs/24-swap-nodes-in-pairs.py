# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while dummy.next and dummy.next.next:
            d1 = dummy.next
            d2 = dummy.next.next
            dummy.next = d2
            d1.next = d2.next
            d2.next = d1
            dummy = dummy.next.next
        return head.next