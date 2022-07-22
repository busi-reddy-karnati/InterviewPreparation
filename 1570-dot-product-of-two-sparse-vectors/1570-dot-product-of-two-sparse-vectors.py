class SparseVector:
    def __init__(self, nums: List[int]):
        self.size = 0
        self.max_ind = 0
        self.nums = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                self.nums[i] = nums[i]
                self.max_ind = i
                self.size += 1
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        s1 = vec.size
        s2 = self.size
        if s1 > s2:
            ans = 0
            for index in self.nums:
                if index in vec.nums:
                    ans += vec.nums[index]*self.nums[index]
            return ans
        else:
            ans = 0
            for index in vec.nums:
                if index in self.nums:
                    ans += vec.nums[index]*self.nums[index]
            return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)