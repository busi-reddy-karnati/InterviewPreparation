from heapq import heappop,heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for index,list in enumerate(lists):
            if list:
                heappush(heap,(list.val,index, list))
        ans_list = ListNode(0)
        ans_list_tail = ans_list
        while heap:
            val,index,node= heappop(heap)
            ans_list_tail.next = node
            ans_list_tail = ans_list_tail.next
            if node.next:
                heappush(heap,(node.next.val,index,node.next))
        return ans_list.next