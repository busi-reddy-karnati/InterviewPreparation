from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val,i, lists[i]))
                lists[i] = lists[i].next
        dummy = ListNode()
        ans = dummy
        while heap:
            node = heappop(heap)
            i = node[1]
            node = node[2]
            dummy.next = node
            dummy = dummy.next
            if node.next:
                heappush(heap, (node.next.val,i, node.next))
        return ans.next
            