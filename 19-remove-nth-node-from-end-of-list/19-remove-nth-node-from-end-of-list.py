# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        temp = head
        temp2 = head
        for i in range(n):
            temp = temp.next
        if not temp:
            return head.next
        while temp.next!=None:
            temp = temp.next
            temp2 = temp2.next
        temp2.next = temp2.next.next
        return head
        