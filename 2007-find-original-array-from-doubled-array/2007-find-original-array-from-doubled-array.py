from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        num_frequency = defaultdict(int)
        for num in changed:
            num_frequency[num]+=1
        result_array = []
        for num in changed:
            if num == 0:
                if num_frequency[num]%2==1:
                    return []
                for i in range(num_frequency[num]//2):
                    result_array.append(0)
                num_frequency[0] = 0
                continue
            if num_frequency[num] == 0:
                continue
            if num_frequency[2*num] <= 0:
                return []
            result_array.append(num)
            num_frequency[num]-=1
            num_frequency[2*num]-=1
        return result_array
        
        