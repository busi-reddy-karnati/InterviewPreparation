class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0]*length
        for update in updates:
            start_index = update[0]
            end_index = update[1]
            increment = update[2]
            ans[start_index] += increment
            if end_index+1 != length:
                ans[end_index+1]-=increment
        for i in range(1,length):
            ans[i] = ans[i-1]+ans[i]
        return ans
        