class Solution:
    map = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],
          7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
    ans_list = []
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combs = self.letterCombinations(digits[1:])
        if not combs:
            combs.extend(self.map[int(digits[0])])
            return combs
        temp_list = []
        for char in self.map[int(digits[0])]:
            for comb in combs:
                temp_list.append(char+comb)
        return temp_list
        