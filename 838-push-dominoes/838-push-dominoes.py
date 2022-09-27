class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left_sym = "L"
        left_ind = 0
        right_sym = "R"
        right_ind = 0
        ans = list(dominoes)
        i = 0
        while i < len(ans):
            if ans[i] == ".":
                while i < len(ans) and ans[i] == ".":
                    i += 1
                if i == len(ans):
                    right_sym = "R"
                    right_ind = len(ans)
                else:
                    right_sym = ans[i]
                    right_ind = i
                if left_sym == "L" and right_sym == "L":
                    for j in range(left_ind, right_ind):
                        ans[j] = "L"
                elif left_sym == "R" and right_sym == "L":
                    lp = left_ind
                    rp = right_ind
                    while lp < rp:
                        ans[lp] = "R"
                        ans[rp] = "L"
                        lp += 1
                        rp -= 1
                elif left_sym == "R" and right_sym == "R":
                    for j in range(left_ind, right_ind):
                        ans[j] = "R"
                    
            else:
                left_sym = ans[i]
                left_ind = i
                i += 1
        return "".join(ans)