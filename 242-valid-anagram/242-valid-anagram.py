from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for char in s:
            hashmap[char] += 1
        for char in t:
            if hashmap[char] == 0:
                return False
            hashmap[char] -= 1
        return sum(hashmap.values()) == 0