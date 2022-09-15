class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(row, col, match):
            nonlocal board
            if len(match) == 0: # We need to match nothing
                return True
            if row >= len(board) or col >= len(board[0]) or col < 0 or row < 0:
                # print(row, col,match, "1")
                return False
            if board[row][col] != match[0]:
                # print(row, col,match, "2")
                return False
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            board[row][col] = "*"
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if helper(new_row, new_col, match[1:]):
                    return True
            board[row][col] = match[0]
        if not word:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # print("j")
                    if helper(i,j,word):
                        return True
        # print(board)
        return False