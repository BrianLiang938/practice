class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for n in range(9):
            check = {}
            for m in range(9):
                if board[n][m] in check and board[n][m] != '.':
                    return 0
                else:
                    check[board[n][m]] = m
        print("Finished rows")
        for n in range(9):
            check = {}
            for m in range(9):
                if board[m][n] in check and board[m][n] != '.':
                    return 0
                else:
                    check[board[m][n]] = m
        print("Finished columns")
        for n in range(3):           
            for m in range(3):
                check = {}
                for l in range(3):
                    for k in range(3):
                        if board[l + (3*n)][k + (3*m)] in check and board[l + (3*n)][k + (3*m)] != '.':
                            return 0
                        else:
                           check[board[l + (3*n)][k + (3*m)]] = m
        return 1
def main():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print(s.isValidSudoku(board))
    print("Done!")

if __name__ == "__main__":
    main()