# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse_linked_list(head):
    cur = head
    prev = None
    cur_next = head.next
    while cur.next:
        cur.next = prev
        prev = cur
        cur = cur_next
        cur_next = cur.next
    cur.next = prev
    return cur
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        cur_head = head
        next_head = head
        tail = dummy
        while True:
            for i in range(k-1):
                if not next_head.next:
                    tail.next = cur_head
                    return dummy.next
                next_head = next_head.next
            if not next_head.next:
                cur_list = reverse_linked_list(cur_head)
                tail.next = cur_list
                return dummy.next
            temp = next_head.next
            next_head.next = None
            next_head = temp
            cur_list = reverse_linked_list(cur_head)
            tail.next = cur_list
            while tail.next:
                tail = tail.next
            cur_head = next_head
            