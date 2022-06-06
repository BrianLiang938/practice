from operator import truediv


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for n in range(board):
            for m in range(board[0]):
                if board[n][m] == word[0]:
                    self.dfs(x, y, word)
    
    def dfs(self, x, y, word):
        if len(word) == 0:
            return true
        