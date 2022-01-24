class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key= lambda x:len(x))
        index = {}
        ans = [1]*len(words)
        for i,word in enumerate(words):
            index[word] = i
        int_ans = 1
        for ind,word in enumerate(words):
            temp = list(word)
            for i in range(len(temp)):
                small_word = "".join(temp[:i])+"".join(temp[i+1:])
                if small_word in index:
                    ans[ind] = ans[index[small_word]]+1
                    int_ans = max(int_ans,ans[ind])
        return int_ans
        