class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for n in range(len(matrix[0]) - 1):
            for m in range(n, len(matrix)):
                temp = matrix[n][m]
                matrix[n][m] = matrix[m][n]
                matrix[m][n] = temp
        for n in range(len(matrix)):
            matrix[n] = matrix[n][::-1]
