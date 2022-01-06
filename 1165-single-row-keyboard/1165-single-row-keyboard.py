class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hmap = {}
        for i,letter in enumerate(keyboard):
            hmap[letter] = i
        pos = 0
        ans = 0
        for letter in word:
            ans += abs(pos-hmap[letter])
            pos = hmap[letter]
        return ans