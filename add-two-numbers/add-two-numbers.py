# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def len(self,l):
        ans = 0
        while l:
            ans += 1
            l = l.next
        return ans
    def add(self,l,n):
        temp = l
        while l.next:
            l = l.next
        for i in range(n):
            l.next = ListNode(0)
            l = l.next
        return temp
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = l1
        n1 = self.len(l1)
        n2 = self.len(l2)
        if n1 > n2:
            l2 = self.add(l2,abs(n1-n2))
        else:
            l1 = self.add(l1,abs(n1-n2))
        sum = 0
        carry = 0
        while l1.next:
            sum+=l1.val+l2.val+carry
            l1.val = int(sum%10)
            carry = int(sum/10)
            sum = 0
            l1 = l1.next
            l2 = l2.next
        sum = l1.val+l2.val+carry
        l1.val = sum%10
        if sum > 9:
            l1.next = ListNode(sum//10)
        return ans