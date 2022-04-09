class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_elem = nums[0]
        freq = 1
        for i in range(1,len(nums)):
            if freq == 1:
                if maj_elem != nums[i]:
                    maj_elem = nums[i]
                else:
                    freq = 2
            else:
                if maj_elem != nums[i]:
                    freq -= 1
                else:
                    freq += 1
        return maj_elem