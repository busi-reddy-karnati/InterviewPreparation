class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zeros = 0
        p1 = 0
        p2 = 0
        ans = 0
        while p2 < len(nums):
            if nums[p2] == 1:
                p2+=1
                ans = max(ans,p2-p1)
            else:
                num_zeros += 1
                p2+=1
                if num_zeros > k:
                    while nums[p1]!=0:
                        p1+=1
                    p1+=1
                    num_zeros -= 1
        return max(ans,p2-p1)
        