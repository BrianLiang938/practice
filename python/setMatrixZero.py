class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        for n in range(len(matrix)):
            for m in range(len(matrix[0])):
                if matrix[n][m] == 0:
                    row.add(n)
                    col.add(m)
        for r in row:
            for m in range(len(matrix[0])):
                matrix[r][m] = 0
        for c in col:
            for n in range(len(matrix)):
                matrix[n][c] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        