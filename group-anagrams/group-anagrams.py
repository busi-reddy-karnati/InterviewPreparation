class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            if "".join(sorted(word)) in hmap:
                hmap["".join(sorted(word))].append(word)
            else:
                hmap["".join(sorted(word))] = [word]
        return [hmap[i] for i in hmap]