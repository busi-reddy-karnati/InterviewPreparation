class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #maximum on the ends equals minimum on middle
        subArrayLength = len(cardPoints)-k
        minSum = 0
        for i in range(subArrayLength):
            minSum += cardPoints[i]
        ans = minSum
        for i in range(len(cardPoints)-subArrayLength):
            minSum += cardPoints[i+subArrayLength]
            minSum -= cardPoints[i]
            ans = min(minSum,ans)
        return sum(cardPoints)-ans