from queue import Queue
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = Queue()
        visited = set()
        queue.put(start)
        visited.add(start)
        while queue.qsize()>0:
            elem = queue.get()
            if arr[elem] == 0:
                return True
            if arr[elem] + elem < len(arr) and arr[elem]+elem not in visited:
                queue.put(arr[elem]+elem)
                visited.add(arr[elem]+elem)
            if elem - arr[elem] >= 0 and elem-arr[elem] not in visited:
                queue.put(elem-arr[elem])
                visited.add(elem-arr[elem])
        return False