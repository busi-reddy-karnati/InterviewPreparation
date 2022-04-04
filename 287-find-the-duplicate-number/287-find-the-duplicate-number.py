class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Brute force: keep a hashmap and keep checking each one,
        if you see that there is an element more than once, then return
        Time: N
        Space: N
        
        Better: sort and see if each one is equal to beside
        Time: NlogN
        Space: N
        
        Better2: sum(array)-sum(set(array))
        Time: N
        space: N
        
        
        Best:
        for each number, index = abs(number)-1
        make that index as -(num at that index)
        if already negative then, return        
        
        '''
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] < 0:
                return index+1
            nums[index] = -nums[index]
        