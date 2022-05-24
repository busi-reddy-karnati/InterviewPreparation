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
        head1 = list1
        head2 = list2
        while head1 and head2:
            if head1.val < head2.val:
                if not head1.next:
                    head1.next = head2
                    return list1
                head1 = head1.next
                
            else:
                head1next = head1.next
                head1.next = head2
                head2 = head2.next
                head1.next.next = head1next
                head1.val,head1.next.val = head1.next.val,head1.val
                head1 = head1.next
        return list1
                