class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        numset = set()
        ans = 0
        tempSum = 0
        while ptr2 < len(nums):
            if nums[ptr2] in numset:
                while nums[ptr1] != nums[ptr2]:
                    numset.remove(nums[ptr1])
                    tempSum -= nums[ptr1]
                    ptr1 += 1
                tempSum -= nums[ptr1]
                ptr1+=1
            tempSum += nums[ptr2]
            numset.add(nums[ptr2])
            ptr2 += 1
            ans = max(ans,tempSum)
        return ans