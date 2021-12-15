# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ar = []
        while head:
            ar.append(head.val)
            head = head.next
        ar.sort()
        head = ListNode(0)
        temp = head
        for num in ar:
            temp.next = ListNode(num)
            temp = temp.next
        return head.next