from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = PriorityQueue()
        ans = ListNode(0)
        tail = ans
        for index,head in enumerate(lists):
            if head: q.put((head.val, index, head))
        while q.qsize() > 0:
            elem = q.get()
            tail.next = ListNode(elem[0])
            tail = tail.next
            if elem[2].next:
                q.put((elem[2].next.val,elem[1],elem[2].next))
            
        return ans.next