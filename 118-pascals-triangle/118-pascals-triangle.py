class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        row = [1]
        for i in range(numRows-1):
            next_row = [1]
            for j in range(len(row)-1):
                next_row.append(row[j]+row[j+1])
            next_row.append(1)
            ans.append(next_row)
            row = [num for num in next_row]
        return ans
        