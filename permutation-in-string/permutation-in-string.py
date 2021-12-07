class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        map1 = {}
        for char in s1:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1
        map2 = {}
        for i in range(len(s1)):
            char = s2[i]
            if char in map2:
                map2[char] += 1
            else:
                map2[char] = 1
        if map1 == map2:
            return True
        n = len(s1)
        for i in range(len(s2)-len(s1)):
            if s2[i] in map2:
                if map2[s2[i]] == 1:
                    map2.pop(s2[i])
                else:
                    map2[s2[i]] -=1
            print(n+i)
            if s2[n+i] in map2:
                map2[s2[n+i]]+=1
            else:
                map2[s2[n+i]] = 1
            if map1 == map2:
                return True
        return False