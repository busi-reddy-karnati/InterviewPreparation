class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0]*26
        s2_map = [0]*26
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            index = ord(s1[i])-ord("a")
            s1_map[index] += 1
            index = ord(s2[i])-ord("a")
            s2_map[index] += 1
        matches = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                matches += 1
        if matches == 26:
            return True
        
        for i in range(len(s2)-len(s1)):
            #char to add
            char = s2[i+len(s1)]
            index = ord(char)-ord("a")
            s2_map[index] += 1
            if s2_map[index]-1 == s1_map[index]:
                matches -= 1
            elif s2_map[index] == s1_map[index]:
                matches += 1
            
            #char to remove
            char = s2[i]
            index = ord(char)-ord("a")
            s2_map[index] -= 1
            if s2_map[index]+1 == s1_map[index]:
                matches -= 1
            elif s2_map[index] == s1_map[index]:
                matches += 1
            if matches == 26:
                return True
            
        return False