# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast_pointer = head.next
        slow_pointer = head
        while slow_pointer and fast_pointer:
            if slow_pointer == fast_pointer:
                return True
            slow_pointer = slow_pointer.next
            if fast_pointer.next:
                fast_pointer = fast_pointer.next.next
            else:
                return False
        return False
        