class MyCalendar:

    def __init__(self):
        self.slots = set()

    def book(self, start: int, end: int) -> bool:
        for slot in self.slots:
            st = slot[0]
            en = slot[1]
            if start<st<end or start<en<end or (start>=st and end<=en):
                return False
        self.slots.add((start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)