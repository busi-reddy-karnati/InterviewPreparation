class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        map = {}
        for i,char in enumerate(keyboard):
            map[char] = i
        ans = 0
        if not word:
            return 0
        ans += map[word[0]]
        for i in range(len(word)-1):
            ans += abs(map[word[i+1]]-map[word[i]])
        return ans