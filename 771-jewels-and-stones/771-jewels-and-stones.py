class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        ans = sum(1 for char in stones if char in jewels)
        return ans