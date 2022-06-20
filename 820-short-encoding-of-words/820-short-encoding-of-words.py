class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda a:a[::-1])
        ans = 0
        for i in range(len(words)-1):
            if words[i+1].endswith(words[i]):
                continue
            ans+=len(words[i])+1
        ans += len(words[-1])+1
        return ans
            