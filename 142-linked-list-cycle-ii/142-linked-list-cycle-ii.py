# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast:
            if not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast:
            return None
        slow = head
        # print(fast, slow)
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
            