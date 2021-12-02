class Solution:
    def search(self, a: List[int], target: int) -> int:
        first = 0
        last = len(a)-1
        while first<=last:
            mid = int((first+last)/2)
            if a[mid] == target:
                return mid
            if a[last] < a[mid]:
                if a[mid]<target:
                    first = mid+1
                else:
                    if a[last] < target:
                        last = mid-1
                    else:
                        first = mid+1
            else:
                if a[mid] > target:
                    last = mid-1
                else:
                    if a[last] >= target:
                        first = mid+1
                    else:
                        last = mid-1
        return -1
            
            