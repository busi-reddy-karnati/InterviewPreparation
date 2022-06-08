# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getLen(head):
    temp = head
    ans = 0
    while temp:
        ans += 1
        temp = temp.next
    return ans
def add(head,n):
    temp = head
    while temp.next:
        temp = temp.next
    for i in range(n):
        newNode = ListNode(0)
        temp.next = newNode
        temp = temp.next
    
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = getLen(l1)
        n2 = getLen(l2)
        if n1>n2:
            add(l2,n1-n2)
        else:
            add(l1,n2-n1)
        carry = 0
        sum = 0
        ptr1 = l1
        ptr2 = l2
        
        while ptr1.next:
            sum = ptr1.val+ptr2.val+carry
            carry = sum//10
            sum = sum%10
            ptr1.val = sum
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        sum = ptr1.val+ptr2.val+carry
        carry = sum//10
        sum = sum%10
        ptr1.val = sum
        if carry > 0:
            ptr1.next = ListNode(carry)
        return l1