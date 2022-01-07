class Solution:
    def countLetters(self, s: str) -> int:
        if not s:
            return 0
        buffer = s[0]
        ans = 0
        count = 1
        for i in range(1,len(s)):
            char = s[i]
            # print(ans)
            if char == buffer:
                count+=1
            else:
                ans += (count*(count+1))//2
                # print(count)
                count = 1
                buffer = char
        ans += (count*(count+1))//2
        return ans
        