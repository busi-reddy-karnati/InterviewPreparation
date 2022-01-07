class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self, n):
        self.head = None
        self.tail = None
        self.capacity = n
        self.sum = 0
        self.total_nodes = 0
    def add_node(self,val):
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
            self.sum+=val
            self.total_nodes += 1
            return val
        if self.capacity == self.total_nodes:
            self.sum -= self.head.val
            self.head = self.head.next
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.sum+=self.tail.val
            return self.sum/self.capacity
        else:
            self.sum+=val
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.total_nodes+=1
            return self.sum/self.total_nodes
    
    
class MovingAverage:

    def __init__(self, size: int):
        self.ll = LinkedList(size)

    def next(self, val: int) -> float:
        return self.ll.add_node(val)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)