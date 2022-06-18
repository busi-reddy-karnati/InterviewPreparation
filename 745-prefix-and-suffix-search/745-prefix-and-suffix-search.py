from collections import defaultdict
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.indices = {}
        for i,word in enumerate(words):
            self.indices[word] = i
            prefix = ''
            suffix = ''
            for char in ['']+list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in ['']+list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
        
    def f(self, prefix: str, suffix: str) -> int:
        ans = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.indices[word] > ans:
                ans = self.indices[word]
        return ans


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)