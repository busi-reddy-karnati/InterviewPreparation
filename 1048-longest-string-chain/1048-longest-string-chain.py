class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word:-len(word))
        word_set = set()
        for word in words:
            word_set.add(word)
        hashmap = {}
        for word in words:
            if word in hashmap:
                chain_length = hashmap[word]
            else:
                chain_length = 1
            for i in range(len(word)):
                temp_word = word[:i]+word[i+1:]
                if temp_word in word_set:
                    if temp_word in hashmap:
                        hashmap[temp_word] = max(chain_length+1,hashmap[temp_word])
                    else:
                        hashmap[temp_word] = chain_length+1
        if not hashmap:
            return 1
        print(hashmap)
        return max(hashmap.values())