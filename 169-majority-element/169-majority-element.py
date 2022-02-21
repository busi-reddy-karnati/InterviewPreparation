class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = 1
        nummax = nums[0]
        for num in nums:
            if num == nummax:
                freq+=1
            else:
                if freq == 1:
                    nummax = num
                else:
                    freq -= 1
        return nummax