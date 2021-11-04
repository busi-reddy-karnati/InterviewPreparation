class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            ar = [max_product*nums[i],min_product*nums[i],nums[i]]
            
            max_product = max(ar)
            min_product = min(ar)
            ans = max(ans,max_product)
            # print(ans)
            # print("index {} max {} min {}".format(i,max_product,min_product))
        return ans
        