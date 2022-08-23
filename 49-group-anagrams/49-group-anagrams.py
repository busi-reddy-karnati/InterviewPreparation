class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def string_map(s):
            li = [0 for i in range(26)] #For each char
            for char in s:
                li[ord(char)-ord('a')] += 1
            tu = tuple(li)
            return tu
        hmap = {}
        for string in strs:
            str_tu = string_map(string)
            if str_tu in hmap:
                hmap[str_tu].append(string)
            else:
                hmap[str_tu] = [string]
        return list(hmap.values())