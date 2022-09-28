# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        temp = head
        for i in range(n+1):
            temp = temp.next
        ptr = head
        while temp:
            ptr = ptr.next
            temp = temp.next
        ptr.next = ptr.next.next
        return head.next