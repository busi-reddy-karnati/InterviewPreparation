# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        ans = list1
        list1_prev = None
        while list1 and list2:
            if list1.val < list2.val:
                list1_prev = list1
                list1 = list1.next
            else:
                list1_next = list1.next
                list1.next = list2
                list2 = list2.next
                list1.next.next = list1_next
                list1.next.val, list1.val = list1.val, list1.next.val
                list1_prev = list1
                list1 = list1.next
        if not list1:
            list1_prev.next = list2
        return ans