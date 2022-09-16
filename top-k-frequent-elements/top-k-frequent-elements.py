class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def swap(i,j):
            nonlocal arr
            arr[i], arr[j] = arr[j], arr[i]
        hm = {}
        for num in nums:
            hm[num] = hm.get(num,0)+1
        arr = []
        for ke in hm:
            arr.append([hm[ke], ke])
        left = 0
        right = len(arr)-1
        pivot = -1
        target_pos = len(arr)-k
        # print(arr)
        while pivot != target_pos:
            ptr = left
            for i in range(left, right):
                if arr[i][0] <= arr[right][0]:
                    swap(i,ptr)
                    ptr += 1
            swap(right, ptr)
            pivot = ptr
            if pivot < target_pos:
                left = pivot + 1
            else:
                right = pivot - 1
        ans = []
        # print(arr, pivot, target_pos,k)
        for i in range(pivot,len(arr)):
            ans.append(arr[i][1])
        return ans