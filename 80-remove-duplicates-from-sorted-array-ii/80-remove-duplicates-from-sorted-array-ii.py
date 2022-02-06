class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0
        pointer2 = 0
        temp_num = nums[0]
        temp_freq = 0
        while pointer2 < len(nums):
            if nums[pointer2] == temp_num:
                if temp_freq > 1:
                    pointer2+=1
                else:
                    nums[pointer1] = temp_num
                    temp_freq += 1
                    pointer1 += 1
                    pointer2 += 1
            else:
                nums[pointer1] = nums[pointer2]
                temp_num = nums[pointer2]
                temp_freq = 1
                pointer2 += 1
                pointer1 += 1
        return pointer1