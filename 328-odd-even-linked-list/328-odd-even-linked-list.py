# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        eh = head.next
        oh = head
        ot, et = oh, eh
        while et and ot and ot.next.next:
            ot.next = et.next
            et.next = ot.next.next
            et = et.next
            ot = ot.next
        ot.next = eh
        return oh
        