# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ans = dummy
        heap = PriorityQueue()
        for i,node in enumerate(lists):
            if node:
                heap.put((node.val,i,node))
        while heap.qsize()>0:
            entry = heap.get()
            index,node = entry[1],entry[2]
            dummy.next = node
            dummy = dummy.next
            if node.next:
                heap.put((node.next.val,index,node.next))
        return ans.next