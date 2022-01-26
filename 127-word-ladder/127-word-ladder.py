from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        visited = set()
        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        distance = {}
        distance[beginWord] = 1
        while queue:
            word = queue.popleft()
            temp = word
            word = list(word)
            for i in range(len(word)):
                char = word[i]
                for j in range(26):
                    ch = chr(ord('a')+j)
                    word[i] = ch
                    new_word = "".join(word)
                    if new_word == endWord and endWord in wordList:
                        return distance[temp]+1
                    if new_word in wordList and new_word not in visited:
                        visited.add(new_word)
                        distance[new_word] = distance[temp]+1
                        queue.append(new_word)
                word[i] = char
        return 0