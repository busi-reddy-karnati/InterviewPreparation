class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mainPtr = m+n-1
        ptr1 = m-1
        ptr2 = n-1
        while mainPtr!=ptr1:
            if ptr1 < 0:
                while mainPtr!=-1:
                    nums1[mainPtr] = nums2[ptr2]
                    ptr2-=1
                    mainPtr-=1
                return
            if nums1[ptr1] > nums2[ptr2]:
                nums1[mainPtr] = nums1[ptr1]
                ptr1-=1
            else:
                nums1[mainPtr] = nums2[ptr2]
                ptr2-=1
            mainPtr -=1
        