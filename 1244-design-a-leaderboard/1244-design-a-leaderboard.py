

class Leaderboard:

    def __init__(self):
        self.leader_board = {}
               

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.leader_board:
            self.leader_board[playerId] += score
        else:
            self.leader_board[playerId] = score
    def top(self, K: int) -> int:
        # print(self.leader_board)
        self.leader_board = dict(sorted(self.leader_board.items(),key=lambda x:x[1],reverse=True))
        # print(self.leader_board)
        i = 0
        ans = 0
        for key in self.leader_board:
            if i == K:
                return ans
            i+=1
            ans+=self.leader_board[key]
        

    def reset(self, playerId: int) -> None:
        self.leader_board[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)