class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage)
                

    def visit(self, url: str) -> None:
        node = Node(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.cur.prev:
                return self.cur.val
            self.cur = self.cur.prev
        return self.cur.val
    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.cur.next:
                return self.cur.val
            self.cur = self.cur.next
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)