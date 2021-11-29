class Solution:
    def helper(self,nums,index):
        nu = 1<<index
        res1 = 0
        res2 = 0
        for num in nums:
            if nu & num:
                res1 = res1^num
            else:
                res2 = res2^num
        return [res1,res2]
                
    def give(self,xor):
        ans = 0
        while xor:
            if xor%2:
                return ans
            ans += 1
            xor = xor//2
        
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor^=num
        return self.helper(nums,self.give(xor))