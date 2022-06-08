class Solution:
    def minSwaps(self, data: List[int]) -> int:
        totalOnes = sum(_ for _ in data)
        numOnes = sum(_ for _ in data[:totalOnes])
        ans = totalOnes-numOnes
        for i in range(len(data)-totalOnes):
            if data[i] == 1:
                numOnes -= 1
            if data[totalOnes+i] == 1:
                numOnes += 1
            replacements = totalOnes - numOnes
            ans = min(ans,replacements)
        return ans