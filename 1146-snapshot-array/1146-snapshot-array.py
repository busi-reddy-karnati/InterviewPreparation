class SnapshotArray:

    def __init__(self, length: int):
        self.a = []
        for i in range(length):
            self.a.append([[-1,0]])
        self.snap_id = 0
    def set(self, index: int, val: int) -> None:
        # print(self.a)
        self.a[index].append([self.snap_id,val])
        # print(self.a)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        # print(self.a[index])
        ar = self.a[index]
        # print(ar)
        lo = 0
        hi = len(ar)-1
        ans = 0
        while hi >= lo:
            mid = (hi+lo)//2
            if ar[mid][0] > snap_id:
                hi = mid-1
            else:
                ans = ar[mid][1]
                lo = mid+1
        return ans
                

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)