from collections import defaultdict
def value(char):
    return ord(char)-ord('a')
class Solution:
    def checkInclusion(self, small_string: str, big_string: str) -> bool:
        count_arr = [0]*26
        if len(small_string) > len(big_string):
            return False
        for i,char in enumerate(small_string):
            count_arr[ord(char)-ord('a')] += 1
            count_arr[ord(big_string[i])-ord('a')] -= 1
        if not any(count_arr):
            return True
        for i in range(len(big_string)-len(small_string)):
            add = big_string[i+len(small_string)]
            rem = big_string[i]
            count_arr[ord(add)-ord('a')] -= 1
            count_arr[ord(rem)-ord('a')] += 1
            if not any(count_arr):
                return True
        return False
        
        