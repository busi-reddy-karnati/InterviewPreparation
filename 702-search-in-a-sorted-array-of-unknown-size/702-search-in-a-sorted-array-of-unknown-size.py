# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:
def bs(arr, target):
    if not arr:
        return -1
    low = 0
    hi = len(arr)-1
    while low <= hi:
        mid = (low+hi)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid-1
        else:
            low = mid+1
    return -1
    
    
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        index = 0
        inc = 1
        while True:
            if reader.get(index) == target:
                return index
            if reader.get(index) > target:
                temp = [0]*(inc)
                for i in range(index-inc,index):
                    temp[i-index+inc] = reader.get(i)
                ans = bs(temp, target)
                if ans == -1:
                    return ans
                return index-inc+ans
            else:
                inc = inc*2
                index = index+inc
        return -1