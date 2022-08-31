# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        if not head:
            return 
        if not head.next and n == 1:
            return head.next
        for i in range(n):
            right = right.next
        if right == None:
            return head.next
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head