# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        head = temp
        while temp:
            for i in range(m):
                temp = temp.next
                if not temp:
                    return head.next
            for i in range(n):
                if not temp.next:
                    return head.next
                temp.next = temp.next.next
        return head.next
        