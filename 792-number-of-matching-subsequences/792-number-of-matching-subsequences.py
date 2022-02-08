from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        charmap = defaultdict(list)
        for word in words:
            charmap[word[0]].append((word,0))
        for char in s:
            templist = charmap[char]
            charmap[char] = []
            for word,index in templist:
                if index+1 == len(word):
                    ans += 1
                else:
                    charmap[word[index+1]].append((word,index+1))
        return ans
        