from operator import truediv


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        out = 0
        for n in range(len(board)):
            for m in range(len(board[0])):
                if board[n][m] == word[0]:
                    out = self.dfs(n, m, word[1:], board, [(n,m)])
                    if out:
                        return out
        return 0
    
    def dfs(self, x, y, word, board, visited):
        out = 0
        if len(word) == 0:
            return 1
        for i, j in ((x-1,y),(x,y-1),(x,y+1),(x+1,y)):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and (i,j) not in visited and board[i][j] == word[0]:
                visited.append((i,j))
                out = self.dfs(i, j, word[1:], board, visited)
                if out == 1:
                    return 1
        return out
#not mine
def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res