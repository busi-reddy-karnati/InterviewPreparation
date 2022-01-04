# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def size(head):
    temp = head
    n =  0
    while temp:
        n+=1
        temp = temp.next
    return n
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = size(l1)
        n2 = size(l2)
        if n1<n2:
            temp = l1
        else:
            temp = l2
        
        while temp.next:
            temp = temp.next
        for i in range(abs(n1-n2)):
            temp.next = ListNode(0)
            temp = temp.next
        carry = 0
        ans = l1
        while l1.next:
            sum = l1.val+l2.val+carry
            carry = sum//10
            sum = sum%10
            l1.val = sum
            l1 = l1.next
            l2 = l2.next
        sum = l1.val+l2.val+carry
        carry = sum//10
        sum%=10
        l1.val = sum
        if carry > 0:
            l1.next = ListNode(carry)
        return ans