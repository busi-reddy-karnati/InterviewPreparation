# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        prev = None
        cur = head
        cur_next = head.next
        while cur_next:
            cur.next = prev
            prev = cur
            cur = cur_next
            cur_next = cur.next
        cur.next = prev
        return cur