def giveSortedString(s):
    s = list(s)
    s.sort()
    return "".join(s)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOfAnagrams = {}
        for string in strs:
            modifiedString = giveSortedString(string)
            if modifiedString in mapOfAnagrams:
                mapOfAnagrams[modifiedString].append(string)
            else:
                mapOfAnagrams[modifiedString] = [string]
        return mapOfAnagrams.values()
        