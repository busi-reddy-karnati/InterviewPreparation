# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        evenhead = head.next
        oddtail = head
        eventail = head.next
        while eventail and eventail.next:
            oddtail.next = eventail.next
            oddtail = oddtail.next
            eventail.next = oddtail.next
            eventail = oddtail.next
            
        oddtail.next = evenhead
        return head