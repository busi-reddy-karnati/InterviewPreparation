class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        for i,num in enumerate(nums2):
            hmap[num] = i
        for i in range(len(nums1)):
            nums1[i] = hmap[nums1[i]]
        return nums1
            
        