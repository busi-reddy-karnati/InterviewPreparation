import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_freq = {}
        banned = set(banned)
        word_buffer = []
        for i in range(len(paragraph)):
            char = paragraph[i]
            if not char.isalnum() and word_buffer:
                word = "".join(word_buffer)
                if word not in banned:
                    word_freq[word] = word_freq.get(word,0)+1
                word_buffer = []
            elif char.isalnum():
                word_buffer.append(char.lower())
        if word_buffer:
            word = "".join(word_buffer)
            if word not in banned  and word!="":
                word_freq[word] = word_freq.get(word,0)+1
            word_buffer = []
        most_freq = 0
        ans = ""
        for word in word_freq:
            if word_freq[word] > most_freq:
                ans = word
                most_freq = word_freq[word]
        print(word_freq)
        return ans
                