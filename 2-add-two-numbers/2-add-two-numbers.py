# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        temp = head
        ans = 0
        while temp:
            ans += 1
            temp = temp.next
        return ans
    def add_dummy_nodes(self, head, n):
        temp = head
        while temp.next:
            temp = temp.next
        for i in range(n):
            temp.next = ListNode(0)
            temp = temp.next
        return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.length(l1) 
        n2 = self.length(l2)
        if n1 < n2:
            self.add_dummy_nodes(l1, abs(n1-n2))
        else:
            self.add_dummy_nodes(l2, abs(n1-n2))
        ans = l1
        carry = 0
        tail = l1
        while l1 and l2:
            sum_of_nodes = l1.val+l2.val+carry
            carry = sum_of_nodes // 10
            sum_of_nodes = sum_of_nodes%10
            l1.val = sum_of_nodes    
            tail = l1
            l1 = l1.next
            l2 = l2.next
        if carry:
            tail.next = ListNode(carry)
        return ans
        