class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x : len(x),reverse=True)
        ans = {}
        for word in words:
            ans[word] = 1
        
        for word in words:
            for i in range(len(word)):
                temp_str = word[:i] + word[i+1:]
                if temp_str in ans:
                    ans[temp_str] = max(ans[word] + 1,ans[temp_str])
        return max(ans.values())
        