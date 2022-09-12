class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        least_diff = float("inf")
        ans = 0
        for i in range(len(nums)):
            # print(i)
            left = i+1
            right = len(nums)-1
            while left < right:
                sum_ = nums[i] + nums[left]+nums[right]
                # print(i,left,right, sum_)
                if sum_ == target:
                    return target
                if abs(target-sum_) < least_diff:
                        ans = sum_
                        least_diff = abs(target-sum_)
                if sum_ > target:
                    right -= 1
                else:
                    left += 1
        return ans