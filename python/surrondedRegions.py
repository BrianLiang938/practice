class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = []
        for n in range(len(board)):
            for m in range(len(board)):
                if board[n][m] == "O" and (n,m) not in visited:
                    visited.append((n,m))
                    self.dfs(board, n, m, visited)
    
    def dfs(self, board, i, j, visited):
        if i == len(board) - 1 or j == len(board) - 1 or i == 0 or j == 0 and board[i][j] == "X":
            return 0
        flag = 1
        for x, y in ((i-1,j),(i,j-1),(i,j+1),(i+1,j)):
            if 0 <= x < len(board) and 0 <= y < len(board) and board[x][y] == "O" and (x,y) not in visited:
                visited.append((x,y))
                flag = self.dfs(board, x, y, visited)
                if flag:
                    board[x][y] = "X"
        if flag:
            board[i][j] = "X"
        return 1

# discuss solution
class Solution(object):
    # DFS
    def solve1(self, board):
        if not board or not board[0]:
            return 
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                self.dfs(board, i, j)   
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                self.dfs(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '.':
                    board[i][j] = 'O'
                
    def dfs(self, board, i, j):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = '.'
            self.dfs(board, i+1, j)
            self.dfs(board, i-1, j)
            self.dfs(board, i, j+1)
            self.dfs(board, i, j-1)