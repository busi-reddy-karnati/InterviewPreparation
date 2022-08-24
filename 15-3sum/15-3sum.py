class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            low = i+1
            high = len(nums)-1
            while (high > low):
                sum = nums[high]+nums[low]+nums[i]
                if sum == 0:
                    ans.append([nums[high], nums[low], nums[i]])
                    #Don't use the same number again
                    while nums[low] == nums[low+1] and low+1<high:
                        low = low + 1
                    low = low + 1
                elif sum > 0:
                    high -= 1
                else:
                    low += 1
        return ans