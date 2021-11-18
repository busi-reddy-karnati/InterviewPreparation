class Solution:
    def numDecodings(self, s: str) -> int:   
        self.hmap={}
        return self.helper(s,0)
    def helper(self,s,index):    
        if index == 0:
            self.hmap={}
        if index in self.hmap:
            return self.hmap[index]
        if index>=len(s):
            return 1
        if s[index] == '0':
            return 0
        if index == len(s)-1:
            return 1
        num = int(s[index])
        if num == 1:
            ans = self.helper(s,index+1)+self.helper(s,index+2)
            self.hmap[index] = ans
            return ans
        elif num == 2:
            if int(s[index+1]) > 6:
                ans = self.helper(s,index+1)
                self.hmap[index] = ans
                return ans
            else:
                ans = self.helper(s,index+1)+self.helper(s,index+2)
                self.hmap[index] = ans
                return ans
        else:
            return self.helper(s,index+1)
