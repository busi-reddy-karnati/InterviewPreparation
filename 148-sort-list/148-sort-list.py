# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        nums.sort()
        head = ListNode(0)
        dummy = head
        for i in range(len(nums)):
            dummy.next = ListNode(nums[i])
            dummy = dummy.next
        return head.next
        