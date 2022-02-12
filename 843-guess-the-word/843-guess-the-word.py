# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
import random
def find_matches(str1,str2):
    ans = 0
    for i in range(6):
        if str1[i] == str2[i]:
            ans += 1
    return ans
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        processed = [False]*len(wordlist)
        index = random.randint(0,len(wordlist)-1)
        while True:
            if all(processed):
                return
            while processed[index]:
                index = random.randint(0,len(wordlist)-1)
            print("hi")
            word = wordlist[index]
            processed[index] = True
            matches = master.guess(word)
            if matches == 6:
                return 
            for i in range(len(wordlist)):
                if not processed[i]:
                    temp_matches = find_matches(word,wordlist[i])
                    print(temp_matches,matches,word,wordlist[i])
                    if temp_matches != matches:
                        processed[i] = True
            
            
            
        